<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-Powered Resume Analyzer and Builder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            margin-top: 20px;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        code {
            background-color: #e8ecef;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
        }
        pre {
            background-color: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .section {
            background-color: #fff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .highlight {
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="section">
        <h1>AI-Powered Resume Analyzer and Builder</h1>

        <h2>Overview</h2>
        <p>This project is an AI-powered web application designed to streamline the resume creation and analysis process for job seekers. It integrates a resume analyzer, resume builder, statistics dashboard, feedback system, and an Ollama-powered chatbot, all backed by a MySQL database. The application leverages natural language processing (NLP) and machine learning to provide actionable insights, optimize resumes for Applicant Tracking Systems (ATS), and enhance job application success.</p>

        <h2>Features</h2>

        <h3>1. Resume Analyzer</h3>
        <ul>
            <li><span class="highlight">PDF Parsing</span>: Extracts text from uploaded resumes in PDF format using libraries like PyPDF2.</li>
            <li><span class="highlight">Keyword Extraction</span>: Identifies key skills, certifications, and experiences using NLP techniques.</li>
            <li><span class="highlight">Job Description Matching</span>: Compares resumes against job descriptions to highlight gaps and suggest improvements.</li>
            <li><span class="highlight">ATS Compatibility Scoring</span>: Evaluates how well the resume aligns with ATS requirements.</li>
            <li><span class="highlight">Skill Recommendations</span>: Suggests additional skills to include based on job roles.</li>
        </ul>

        <h3>2. Resume Builder</h3>
        <ul>
            <li><span class="highlight">Customizable Templates</span>: Offers multiple professional resume templates for users to customize.</li>
            <li><span class="highlight">Real-Time Preview</span>: Displays resume updates in real-time as users input data.</li>
            <li><span class="highlight">PDF Export</span>: Allows users to download their polished resumes in PDF format.</li>
            <li><span class="highlight">AI-Driven Suggestions</span>: Provides content recommendations to optimize resume sections like work experience, skills, and achievements.</li>
        </ul>

        <h3>3. Statistics Data Dashboard</h3>
        <ul>
            <li><span class="highlight">Keyword Analysis</span>: Visualizes keyword frequency and relevance for specific job roles.</li>
            <li><span class="highlight">Skills Gap Analysis</span>: Displays gaps between user skills and job requirements through interactive charts.</li>
            <li><span class="highlight">Resume Score Trends</span>: Tracks improvements in resume scores over time.</li>
            <li><span class="highlight">Job Match Percentage</span>: Shows how well a resume matches various job descriptions.</li>
        </ul>

        <h3>4. Feedback System</h3>
        <ul>
            <li><span class="highlight">Personalized Feedback</span>: Offers detailed suggestions for improving resume content and structure.</li>
            <li><span class="highlight">Role-Based Insights</span>: Provides tailored advice based on the target job position.</li>
            <li><span class="highlight">Real-Time Feedback</span>: Updates suggestions as users modify their resumes.</li>
        </ul>

        <h3>5. Ollama Chatbot</h3>
        <ul>
            <li><span class="highlight">AI-Powered Assistance</span>: Powered by the Ollama framework, the chatbot provides real-time guidance for resume creation and optimization.</li>
            <li><span class="highlight">Career Advice</span>: Answers user queries about job applications, interview preparation, and skill development.</li>
            <li><span class="highlight">Interactive Support</span>: Engages with users to clarify requirements and suggest improvements.</li>
        </ul>

        <h3>6. MySQL Database</h3>
        <ul>
            <li><span class="highlight">Data Storage</span>: Stores user profiles, resumes, job descriptions, and analysis results.</li>
            <li><span class="highlight">Efficient Queries</span>: Supports fast retrieval of data for real-time dashboard updates and chatbot responses.</li>
            <li><span class="highlight">Scalability</span>: Handles large datasets for multiple users and job applications.</li>
        </ul>

        <h2>Tech Stack</h2>
        <ul>
            <li><span class="highlight">Frontend</span>: React.js, Tailwind CSS</li>
            <li><span class="highlight">Backend</span>: Python, FastAPI</li>
            <li><span class="highlight">Database</span>: MySQL</li>
            <li><span class="highlight">AI/NLP</span>: Ollama, Hugging Face Transformers (e.g., BERT for NER), LangChain</li>
            <li><span class="highlight">PDF Processing</span>: PyPDF2</li>
            <li><span class="highlight">Dashboard</span>: Streamlit for interactive visualizations</li>
            <li><span class="highlight">Other Libraries</span>: Scikit-learn, NLTK, Pandas</li>
        </ul>

        <h2>Installation</h2>

        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.8+</li>
            <li>MySQL Server</li>
            <li>Node.js and npm</li>
            <li>Git</li>
            <li>Ollama (for chatbot functionality)</li>
        </ul>

        <h3>Steps</h3>
        <ol>
            <li><span class="highlight">Clone the Repository</span>:
                <pre><code>git clone https://github.com/Dharaneesh05/AI-powered-resume-analyzer-builder.git
cd AI-powered-resume-analyzer-builder</code></pre>
            </li>
            <li><span class="highlight">Set Up Backend</span>:
                <ul>
                    <li>Install Python dependencies:
                        <pre><code>pip install -r requirements.txt</code></pre>
                    </li>
                    <li>Configure MySQL:
                        <ul>
                            <li>Create a database named <code>resume_analyzer</code>.</li>
                            <li>Update database credentials in <code>config.py</code>:
                                <pre><code>DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'resume_analyzer'
}</code></pre>
                            </li>
                            <li>Run database migrations:
                                <pre><code>python migrate.py</code></pre>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li><span class="highlight">Set Up Frontend</span>:
                <ul>
                    <li>Navigate to the frontend directory:
                        <pre><code>cd frontend</code></pre>
                    </li>
                    <li>Install dependencies:
                        <pre><code>npm install</code></pre>
                    </li>
                    <li>Start the frontend server:
                        <pre><code>npm start</code></pre>
                    </li>
                </ul>
            </li>
            <li><span class="highlight">Set Up Ollama</span>:
                <ul>
                    <li>Install Ollama following the official documentation: <a href="https://ollama.ai/docs/installation">Ollama Installation Guide</a>.</li>
                    <li>Pull the required model (e.g., LLaMA):
                        <pre><code>ollama pull llama3</code></pre>
                    </li>
                    <li>Configure the chatbot endpoint in <code>config.py</code>.</li>
                </ul>
            </li>
            <li><span class="highlight">Run the Application</span>:
                <ul>
                    <li>Start the backend server:
                        <pre><code>uvicorn app.main:app --reload</code></pre>
                    </li>
                    <li>Start the Streamlit dashboard:
                        <pre><code>streamlit run dashboard.py</code></pre>
                    </li>
                </ul>
            </li>
            <li><span class="highlight">Access the Application</span>:
                <ul>
                    <li>Frontend: <a href="http://localhost:3000">http://localhost:3000</a></li>
                    <li>Dashboard: <a href="http://localhost:8501">http://localhost:8501</a></li>
                    <li>API: <a href="http://localhost:8000">http://localhost:8000</a></li>
                </ul>
            </li>
        </ol>

        <h2>Usage</h2>
        <ol>
            <li><span class="highlight">Upload Resume</span>: Upload a PDF resume or create one from scratch using the resume builder.</li>
            <li><span class="highlight">Analyze Resume</span>: The system extracts key information, scores ATS compatibility, and suggests improvements.</li>
            <li><span class="highlight">View Dashboard</span>: Check the statistics dashboard for keyword and skills gap analysis.</li>
            <li><span class="highlight">Interact with Chatbot</span>: Use the Ollama chatbot for real-time guidance and career advice.</li>
            <li><span class="highlight">Export Resume</span>: Download the optimized resume as a PDF.</li>
        </ol>

        <h2>Contributing</h2>
        <p>We welcome contributions! To contribute:</p>
        <ol>
            <li>Fork the repository.</li>
            <li>Create a feature branch (<code>git checkout -b feature/YourFeature</code>).</li>
            <li>Commit your changes (<code>git commit -m 'Add YourFeature'</code>).</li>
            <li>Push to the branch (<code>git push origin feature/YourFeature</code>).</li>
            <li>Open a pull request.</li>
        </ol>
        <p>Please read <code>CONTRIBUTING.md</code> for more details.</p>

        <h2>License</h2>
        <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

        <h2>Contact</h2>
        <p>For questions or feedback, reach out via <a href="https://github.com/Dharaneesh05/AI-powered-resume-analyzer-builder/issues">GitHub Issues</a> or email: <a href="mailto:your-email@example.com">your-email@example.com</a>.</p>

        <h2>Acknowledgments</h2>
        <ul>
            <li>Inspired by various open-source resume analysis tools.</li>
            <li>Built with love for job seekers worldwide! 🚀</li>
        </ul>
    </div>
</body>
</html>
