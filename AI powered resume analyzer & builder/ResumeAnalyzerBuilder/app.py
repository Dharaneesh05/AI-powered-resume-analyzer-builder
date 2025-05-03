from flask import Flask, render_template, request, jsonify, send_file, session, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json
import pandas as pd
import io
from datetime import datetime, timedelta
from utils.resume_analyzer import ResumeAnalyzer
from utils.resume_builder import ResumeBuilder
from config.database import get_database_connection, save_resume_data, save_analysis_data, init_database, get_all_analysis
from config.job_roles import JOB_ROLES
from dashboard import DashboardManager
from feedback.feedback import FeedbackManager
import base64
from collections import Counter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = 'your-secret-key'

# Enable CORS for API requests
CORS(app)

# Initialize components
resume_analyzer = ResumeAnalyzer()  # Renamed for clarity
resume_builder = ResumeBuilder()    # Renamed for clarity
dashboard_manager = DashboardManager()
feedback_manager = FeedbackManager()
job_roles = JOB_ROLES

# Initialize database
init_database(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def load_image(image_name):
    """Load image from static directory"""
    try:
        image_path = os.path.join('static', 'assets', image_name)
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        encoded = base64.b64encode(image_bytes).decode()
        return f"data:image/jpeg;base64,{encoded}"
    except Exception as e:
        print(f"Error loading image {image_name}: {e}")
        return None

@app.route('/')
def home():
    session['page'] = 'home'
    return render_template('index.html', session=session)

@app.route('/analyzer', methods=['GET', 'POST'])
def analyzer_route():  # Renamed to avoid conflict with resume_analyzer variable
    session['page'] = 'analyzer'
    if request.method == 'POST':
        try:
            category = request.form.get('category')
            role = request.form.get('role')
            file = request.files.get('resume')
            
            if not file or not category or not role:
                return jsonify({'status': 'error', 'message': 'Missing required fields: file, category, or role'}), 400
            
            # Validate file type
            filename = secure_filename(file.filename)
            if not (filename.endswith('.pdf') or filename.endswith('.docx')):
                return jsonify({'status': 'error', 'message': 'Unsupported file type. Please upload a PDF or DOCX file.'}), 400

            # Extract text based on file type
            text = ""
            if filename.endswith('.pdf'):
                file.seek(0)  # Reset file pointer
                text = resume_analyzer.extract_text_from_pdf(file)
            elif filename.endswith('.docx'):
                # Save the file temporarily to disk since python-docx needs a file path
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                try:
                    text = resume_analyzer.extract_text_from_docx(file_path)
                finally:
                    # Clean up the temporary file
                    if os.path.exists(file_path):
                        os.remove(file_path)
            
            if not text.strip():
                return jsonify({'status': 'error', 'message': 'No text extracted from the resume. Please ensure the file is not empty.'}), 400

            # Analyze resume
            if category not in job_roles or role not in job_roles[category]:
                return jsonify({'status': 'error', 'message': 'Invalid category or role selected.'}), 400

            role_info = job_roles[category][role]
            analysis = resume_analyzer.analyze_resume({'raw_text': text}, role_info)
            
            # Save resume data
            resume_data = {
                'personal_info': {
                    'name': analysis.get('name', ''),
                    'email': analysis.get('email', ''),
                    'phone': analysis.get('phone', ''),
                    'linkedin': analysis.get('linkedin', ''),
                    'github': analysis.get('github', ''),
                    'portfolio': analysis.get('portfolio', '')
                },
                'summary': analysis.get('summary', ''),
                'target_role': role,
                'target_category': category,
                'education': analysis.get('education', []),
                'experience': analysis.get('experience', []),
                'projects': analysis.get('projects', []),
                'skills': analysis.get('skills', []),
                'template': ''
            }
            
            resume_id = save_resume_data(resume_data)
            analysis_data = {
                'resume_id': resume_id,
                'ats_score': analysis['ats_score'],
                'keyword_match_score': analysis['keyword_match']['score'],
                'format_score': analysis['format_score'],
                'section_score': analysis['section_score'],
                'missing_skills': ','.join(analysis['keyword_match']['missing_skills']),
                'recommendations': ','.join(analysis['suggestions'])
            }
            save_analysis_data(resume_id, analysis_data)
            
            session['analytics_data'] = analysis
            session['resume_data'] = resume_data
            session['selected_resume_id'] = resume_id
            
            return jsonify({'status': 'success', 'analysis': session['analytics_data']})
        except Exception as e:
            return jsonify({'status': 'error', 'message': f'Error processing resume: {str(e)}'}), 500
    
    return render_template('analyzer.html', job_roles=job_roles, session=session)

@app.route('/get_roles')
def get_roles():
    category = request.args.get('category')
    if category in job_roles:
        roles = list(job_roles[category].keys())
        return jsonify({'roles': roles})
    return jsonify({'roles': []})

@app.route('/get_role_info')
def get_role_info():
    category = request.args.get('category')
    role = request.args.get('role')
    if category in job_roles and role in job_roles[category]:
        return jsonify(job_roles[category][role])
    return jsonify({'description': '', 'required_skills': []})

@app.route('/builder', methods=['GET', 'POST'])
def builder_route():
    session['page'] = 'builder'
    if request.method == 'POST':
        try:
            # Parse form_data, defaulting to empty dict if not provided
            form_data_json = request.form.get('form_data', '{}')
            form_data = json.loads(form_data_json)
            if not isinstance(form_data, dict):
                raise ValueError("Invalid form data format")

            template = request.form.get('template', 'Modern')
            
            # Ensure form_data has the expected structure with default values
            default_form_data = {
                'personal_info': {
                    'full_name': '',
                    'email': '',
                    'phone': '',
                    'location': '',
                    'linkedin': '',
                    'portfolio': ''
                },
                'summary': '',
                'experience': [],
                'education': [],
                'projects': [],
                'skills_categories': {
                    'technical': [],
                    'soft': [],
                    'languages': [],
                    'tools': []
                },
                'template': 'Modern'
            }
            # Update default_form_data with the submitted form_data
            for key in default_form_data:
                if key not in form_data:
                    form_data[key] = default_form_data[key]
                elif isinstance(default_form_data[key], dict):
                    for subkey in default_form_data[key]:
                        if subkey not in form_data[key]:
                            form_data[key][subkey] = default_form_data[key][subkey]
            
            session['form_data'] = form_data
            
            if not form_data['personal_info']['full_name'] or not form_data['personal_info']['email']:
                return jsonify({'status': 'error', 'message': 'Full name and email are required'}), 400
            
            resume_data = {
                'personal_info': form_data['personal_info'],
                'summary': form_data.get('summary', ''),
                'experience': form_data.get('experience', []),  # Corrected from 'experiences' to 'experience'
                'education': form_data.get('education', []),
                'projects': form_data.get('projects', []),
                'skills': form_data.get('skills_categories', {
                    'technical': [], 'soft': [], 'languages': [], 'tools': []
                }),
                'skills_categories': form_data.get('skills_categories', {
                    'technical': [], 'soft': [], 'languages': [], 'tools': []
                }),
                'template': template
            }
            
            resume_buffer = resume_builder.generate_resume(resume_data)
            if resume_buffer:
                resume_id = save_resume_data(resume_data)
                session['selected_resume_id'] = resume_id
                filename = f"{form_data['personal_info']['full_name'].replace(' ', '_')}_resume.docx"
                return send_file(
                    resume_buffer,
                    download_name=filename,
                    as_attachment=True,
                    mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                )
            else:
                return jsonify({'status': 'error', 'message': 'Failed to generate resume'}), 500
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
    
    # Pass form_data to the template, defaulting to an empty dict if not in session
    form_data = session.get('form_data', {})
    return render_template('builder.html', session=session, form_data=form_data)

@app.route('/generate_resume', methods=['POST'])
def generate_resume_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'education', 'experience', 'skills']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Use the builder instance to generate the resume
        resume_data = {
            'personal_info': {
                'full_name': data['name'],
                'email': data['email'],
                'phone': data['phone']
            },
            'summary': '',
            'experience': data['experience'],
            'education': data['education'],
            'projects': [],
            'skills': {
                'technical': data['skills'],
                'soft': [],
                'languages': [],
                'tools': []
            },
            'skills_categories': {
                'technical': data['skills'],
                'soft': [],
                'languages': [],
                'tools': []
            },
            'template': 'Modern'
        }
        resume_buffer = resume_builder.generate_resume(resume_data)
        if resume_buffer:
            filename = f"{data['name'].replace(' ', '_')}_resume.docx"
            return send_file(
                resume_buffer,
                download_name=filename,
                as_attachment=True,
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
        else:
            return jsonify({"error": "Failed to generate resume"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/dashboard')
def dashboard():
    session['page'] = 'dashboard'

    # Retrieve all analysis data
    analysis_data = get_all_analysis()

    # Calculate metrics
    total_resumes = len(analysis_data)
    avg_ats_score = 0.0
    high_performing = 0
    success_rate = 0.0
    ats_score_distribution = []
    skill_distribution = Counter()
    weekly_submissions = Counter()
    resumes_by_category = Counter()
    recent_resumes = []

    if total_resumes > 0:
        # Calculate average ATS score
        total_ats_score = sum(row['ats_score'] for row in analysis_data)
        avg_ats_score = round(total_ats_score / total_resumes, 2)

        # Count high-performing resumes (ATS score >= 80%)
        high_performing = sum(1 for row in analysis_data if row['ats_score'] >= 80)

        # Calculate success rate
        success_rate = round((high_performing / total_resumes) * 100, 2)

        # ATS score distribution (for a simple chart)
        ats_score_distribution = [0] * 5  # Buckets: 0-20, 20-40, 40-60, 60-80, 80-100
        for row in analysis_data:
            score = row['ats_score']
            if score < 20:
                ats_score_distribution[0] += 1
            elif score < 40:
                ats_score_distribution[1] += 1
            elif score < 60:
                ats_score_distribution[2] += 1
            elif score < 80:
                ats_score_distribution[3] += 1
            else:
                ats_score_distribution[4] += 1

        # Skill distribution (count skills from resume_data)
        for row in analysis_data:
            skills_str = row['skills'] if row['skills'] is not None else ''
            skills = eval(skills_str) if skills_str else []
            if isinstance(skills, dict):
                skills = skills.get('technical', []) + skills.get('soft', [])
            skill_distribution.update(skills)

        # Weekly submission pattern
        today = datetime.now()
        for row in analysis_data:
            upload_date = datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S')
            days_diff = (today - upload_date).days
            week_start = today - timedelta(days=today.weekday())  # Start of current week (Monday)
            if upload_date >= week_start - timedelta(days=28):  # Last 4 weeks
                week_number = (days_diff // 7) + 1
                weekly_submissions[f"Week {week_number}"] += 1

        # Resumes by job category
        for row in analysis_data:
            category = row['target_category']
            resumes_by_category[category] += 1

        # Recent resumes (last 5)
        recent_resumes = [
            {
                'filename': f"Resume_{row['resume_id']}",
                'upload_date': row['created_at'],
                'job_category': row['target_category'],
                'job_role': row['target_role'],
                'ats_score': row['ats_score']
            }
            for row in sorted(analysis_data, key=lambda x: x['created_at'], reverse=True)[:5]
        ]

    dashboard_data = {
        'total_resumes': total_resumes,
        'avg_ats_score': avg_ats_score,
        'high_performing': high_performing,
        'success_rate': success_rate,
        'ats_score_distribution': ats_score_distribution,
        'skill_distribution': dict(skill_distribution.most_common(5)),
        'weekly_submissions': dict(weekly_submissions),
        'resumes_by_category': dict(resumes_by_category),
        'recent_resumes': recent_resumes
    }

    return render_template('dashboard.html', session=session, **dashboard_data)

@app.route('/select_resume/<int:resume_id>')
def select_resume(resume_id):
    session['selected_resume_id'] = resume_id
    return jsonify({'status': 'success'})

@app.route('/job_search')
def job_search():
    session['page'] = 'job_search'
    return render_template('job_search.html', session=session)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    session['page'] = 'feedback'
    if request.method == 'POST':
        try:
            feedback_data = {
                'name': request.form.get('name'),
                'email': request.form.get('email'),
                'rating': int(request.form.get('rating')),
                'comments': request.form.get('comments')
            }
            feedback_manager.save_feedback(feedback_data)
            return jsonify({'status': 'success', 'message': 'Feedback submitted successfully'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
    
    stats = feedback_manager.get_feedback_stats()
    return render_template('feedback.html', session=session, stats=stats)

@app.route('/export_excel')
def export_excel():
    try:
        conn = get_database_connection()
        query = """
            SELECT 
                rd.name, rd.email, rd.phone, rd.linkedin, rd.github, rd.portfolio,
                rd.summary, rd.target_role, rd.target_category,
                rd.education, rd.experience, rd.projects, rd.skills,
                ra.ats_score, ra.keyword_match_score, ra.format_score, ra.section_score,
                ra.missing_skills, ra.recommendations,
                rd.created_at
            FROM resume_data rd
            LEFT JOIN resume_analysis ra ON rd.id = ra.resume_id
        """
        df = pd.read_sql_query(query, conn)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Resume Data')
        conn.close()
        output.seek(0)
        return send_file(
            output,
            download_name='resume_data.xlsx',
            as_attachment=True,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)