AI-Powered Resume Analyzer and Builder
Overview
This project is an AI-powered web application designed to streamline the resume creation and analysis process for job seekers. It integrates a resume analyzer, resume builder, statistics dashboard, feedback system, and an Ollama-powered chatbot, all backed by a MySQL database. The application leverages natural language processing (NLP) and machine learning to provide actionable insights, optimize resumes for Applicant Tracking Systems (ATS), and enhance job application success.
Features
1. Resume Analyzer

PDF Parsing: Extracts text from uploaded resumes in PDF format using libraries like PyPDF2.
Keyword Extraction: Identifies key skills, certifications, and experiences using NLP techniques.
Job Description Matching: Compares resumes against job descriptions to highlight gaps and suggest improvements.
ATS Compatibility Scoring: Evaluates how well the resume aligns with ATS requirements.
Skill Recommendations: Suggests additional skills to include based on job roles.

2. Resume Builder

Customizable Templates: Offers multiple professional resume templates for users to customize.
Real-Time Preview: Displays resume updates in real-time as users input data.
PDF Export: Allows users to download their polished resumes in PDF format.
AI-Driven Suggestions: Provides content recommendations to optimize resume sections like work experience, skills, and achievements.

3. Statistics Data Dashboard

Keyword Analysis: Visualizes keyword frequency and relevance for specific job roles.
Skills Gap Analysis: Displays gaps between user skills and job requirements through interactive charts.
Resume Score Trends: Tracks improvements in resume scores over time.
Job Match Percentage: Shows how well a resume matches various job descriptions.

4. Feedback System

Personalized Feedback: Offers detailed suggestions for improving resume content and structure.
Role-Based Insights: Provides tailored advice based on the target job position.
Real-Time Feedback: Updates suggestions as users modify their resumes.

5. Ollama Chatbot

AI-Powered Assistance: Powered by the Ollama framework, the chatbot provides real-time guidance for resume creation and optimization.
Career Advice: Answers user queries about job applications, interview preparation, and skill development.
Interactive Support: Engages with users to clarify requirements and suggest improvements.

6. MySQL Database

Data Storage: Stores user profiles, resumes, job descriptions, and analysis results.
Efficient Queries: Supports fast retrieval of data for real-time dashboard updates and chatbot responses.
Scalability: Handles large datasets for multiple users and job applications.

Tech Stack

Frontend: React.js, Tailwind CSS
Backend: Python, FastAPI
Database: MySQL
AI/NLP: Ollama, Hugging Face Transformers (e.g., BERT for NER), LangChain
PDF Processing: PyPDF2
Dashboard: Streamlit for interactive visualizations
Other Libraries: Scikit-learn, NLTK, Pandas

Installation
Prerequisites

Python 3.8+
MySQL Server
Node.js and npm
Git
Ollama (for chatbot functionality)

Steps

Clone the Repository:
git clone https://github.com/Dharaneesh05/AI-powered-resume-analyzer-builder.git
cd AI-powered-resume-analyzer-builder


Set Up Backend:

Install Python dependencies:pip install -r requirements.txt


Configure MySQL:
Create a database named resume_analyzer.
Update database credentials in config.py:DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'resume_analyzer'
}


Run database migrations:python migrate.py






Set Up Frontend:

Navigate to the frontend directory:cd frontend


Install dependencies:npm install


Start the frontend server:npm start




Set Up Ollama:

Install Ollama following the official documentation: Ollama Installation Guide.
Pull the required model (e.g., LLaMA):ollama pull llama3


Configure the chatbot endpoint in config.py.


Run the Application:

Start the backend server:uvicorn app.main:app --reload


Start the Streamlit dashboard:streamlit run dashboard.py




Access the Application:

Frontend: http://localhost:3000
Dashboard: http://localhost:8501
API: http://localhost:8000



Usage

Upload Resume: Upload a PDF resume or create one from scratch using the resume builder.
Analyze Resume: The system extracts key information, scores ATS compatibility, and suggests improvements.
View Dashboard: Check the statistics dashboard for keyword and skills gap analysis.
Interact with Chatbot: Use the Ollama chatbot for real-time guidance and career advice.
Export Resume: Download the optimized resume as a PDF.

Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

Please read CONTRIBUTING.md for more details.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or feedback, reach out via GitHub Issues or email: [your-email@example.com].
Acknowledgments

Inspired by various open-source resume analysis tools.
Built with love for job seekers worldwide! 🚀

