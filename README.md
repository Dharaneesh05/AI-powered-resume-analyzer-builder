<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI-Powered Resume Analyzer and Builder</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      line-height: 1.6;
      color: #24292e;
    }
    h1, h2, h3 {
      border-bottom: 1px solid #eaecef;
      padding-bottom: 0.3em;
    }
    code {
      background-color: #f6f8fa;
      padding: 2px 4px;
      border-radius: 3px;
      font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
    }
    pre {
      background-color: #f6f8fa;
      padding: 16px;
      border-radius: 3px;
      overflow-x: auto;
    }
    pre code {
      background: none;
      padding: 0;
    }
    ul {
      padding-left: 20px;
    }
    a {
      color: #0366d6;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .highlight {
      color: #d73a49;
    }
  </style>
</head>
<body>
  <h1>AI-Powered Resume Analyzer and Builder</h1>

  <h2>Overview</h2>
  <p>This project is an AI-powered web application designed to streamline the resume creation and analysis process for job seekers. It integrates a resume analyzer, resume builder, statistics dashboard, feedback system, and an Ollama-powered chatbot, all backed by a MySQL database. The application leverages natural language processing (NLP) and machine learning to provide actionable insights, optimize resumes for Applicant Tracking Systems (ATS), and enhance job application success.</p>

  <h2>Features</h2>
  <h3>1. Resume Analyzer</h3>
  <ul>
    <li><strong class="highlight">PDF Parsing</strong>: Extracts text from uploaded resumes in PDF format using libraries like PyPDF2.</li>
    <li><strong class="highlight">Keyword Extraction</strong>: Identifies key skills, certifications, and experiences using NLP techniques.</li>
    <li><strong class="highlight">Job Description Matching</strong>: Compares resumes against job descriptions to highlight gaps and suggest improvements.</li>
    <li><strong class="highlight">ATS Compatibility Scoring</strong>: Evaluates how well the resume aligns with ATS requirements.</li>
    <li><strong class="highlight">Skill Recommendations</strong>: Suggests additional skills to include based on job roles.</li>
  </ul>

  <h3>2. Resume Builder</h3>
  <ul>
    <li><strong class="highlight">Customizable Templates</strong>: Offers multiple professional resume templates for users to customize.</li>
    <li><strong class="highlight">Real-Time Preview</strong>: Displays resume updates in real-time as users input data.</li>
    <li><strong class="highlight">PDF Export</strong>: Allows users to download their polished resumes in PDF format.</li>
    <li><strong class="highlight">AI-Driven Suggestions</strong>: Provides content recommendations to optimize resume sections like work experience, skills, and achievements.</li>
  </ul>

  <h3>3. Statistics Data Dashboard</h3>
  <ul>
    <li><strong class="highlight">Keyword Analysis</strong>: Visualizes keyword frequency and relevance for specific job roles.</li>
    <li><strong class="highlight">Skills Gap Analysis</strong>: Displays gaps between user skills and job requirements through interactive charts.</li>
    <li><strong class="highlight">Resume Score Trends</strong>: Tracks improvements in resume scores over time.</li>
    <li><strong class="highlight">Job Match Percentage</strong>: Shows how well a resume matches various job descriptions.</li>
  </ul>

  <h3>4. Feedback System</h3>
  <ul>
    <li><strong class="highlight">Personalized Feedback</strong>: Offers detailed suggestions for improving resume content and structure.</li>
    <li><strong class="highlight">Role-Based Insights</strong>: Provides tailored advice based on the target job position.</li>
    <li><strong class="highlight">Real-Time Feedback</strong>: Updates suggestions as users modify their resumes.</li>
  </ul>

  <h3>5. Ollama Chatbot</h3>
  <ul>
    <li><strong class="highlight">AI-Powered Assistance</strong>: Powered by the Ollama framework, the chatbot provides real-time guidance for resume creation and optimization.</li>
    <li><strong class="highlight">Career Advice</strong>: Answers user queries about job applications, interview preparation, and skill development.</li>
    <li><strong class="highlight">Interactive Support</strong>: Engages with users to clarify requirements and suggest improvements.</li>
  </ul>

  <h3>6. MySQL Database</h3>
  <ul>
    <li><strong class="highlight">Data Storage</strong>: Stores user profiles, resumes, job descriptions, and analysis results.</li>
    <li><strong class="highlight">Efficient Queries</strong>: Supports fast retrieval of data for real-time dashboard updates and chatbot responses.</li>
    <li><strong class="highlight">Scalability</strong>: Handles large datasets for multiple users and job applications.</li>
  </ul>

  <h2>Tech Stack</h2>
  <ul>
    <li><strong class="highlight">Frontend</strong>: React.js, Tailwind CSS</li>
    <li><strong class="highlight">Backend</strong>: Python, FastAPI</li>
    <li><strong class="highlight">Database</strong>: MySQL</li>
    <li><strong class="highlight">AI/NLP</strong>: Ollama, Hugging Face Transformers (e.g., BERT for NER), LangChain</li>
    <li><strong class="highlight">PDF Processing</strong>: PyPDF2</li>
    <li><strong class="highlight">Dashboard</strong>: Streamlit for interactive visualizations</li>
    <li><strong class="highlight">Other Libraries</strong>: Scikit-learn, NLTK, Pandas</li>
  </ul>

  <h2>Installation</h2>
  <p>To set up and run the project locally, follow these steps:</p>
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
    <li><strong class="highlight">Clone the Repository</strong>:
      <pre><code>git clone https://github.com/Dharaneesh05/AI-powered-resume-analyzer-builder.git
cd AI-powered-resume-analyzer-builder</code></pre>
    </li>
    <li><strong class="highlight">Set Up Backend</strong>:
      <p>Install Python dependencies:</p>
      <pre><code>pip install -r requirements.txt</code></pre>
      <p>Configure MySQL:</p>
      <ul>
        <li>Create a database named <code>resume_analyzer</code>.</li>
        <li>Update database credentials in <code>config.py</code>:</li>
        <pre><code class="language-python">DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'resume_analyzer'
}</code></pre>
        <li>Run database migrations:</li>
        <pre><code>python migrate.py</code></pre>
      </ul>
    </li>
    <li><strong class="highlight">Set Up Frontend</strong>:
      <p>Navigate to the frontend directory:</p>
      <pre><code>cd frontend</code></pre>
      <p>Install dependencies:</p>
      <pre><code>npm install</code></pre>
      <p>Start the frontend server:</p>
      <pre><code>npm start</code></pre>
    </li>
    <li><strong class="highlight">Set Up Ollama</strong>:
      <ul>
        <li>Install Ollama following the official documentation: <a href="https://ollama.ai/docs/installation">Ollama Installation Guide</a>.</li>
        <li>Pull the required model (e.g., LLaMA):</li>
        <pre><code>ollama pull llama3</code></pre>
        <li>Configure the chatbot endpoint in <code>config.py</code>.</li>
      </ul>
    </li>
    <li><strong class="highlight">Run the Application</strong>:
      <p>Start the backend server:</p>
      <pre><code>uvicorn app.main:app --reload</code></pre>
      <p>Start the Streamlit dashboard:</p>
      <pre><code>streamlit run dashboard.py</code></pre>
    </li>
    <li><strong class="highlight">Access the Application</strong>:
      <ul>
        <li>Frontend: <a href="http://localhost:3000">http://localhost:3000</a></li>
        <li>Dashboard: <a href="http://localhost:8501">http出來

System: <xaiArtifact artifact_id="be0c5bc4-d2be-40b8-91ae-e8195edd34b1" artifact_version_id="74b69a08-f5a1-435d-952e-afbd95ee0193" title="README.html" contentType="text/html">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI-Powered Resume Analyzer and Builder</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      line-height: 1.6;
      color: #24292e;
    }
    h1, h2, h3 {
      border-bottom: 1px solid #eaecef;
      padding-bottom: 0.3em;
    }
    code {
      background-color: #f6f8fa;
      padding: 2px 4px;
      border-radius: 3px;
      font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
    }
    pre {
      background-color: #f6f8fa;
      padding: 16px;
      border-radius: 3px;
      overflow-x: auto;
    }
    pre code {
      background: none;
      padding: 0;
    }
    ul {
      padding-left: 20px;
    }
    a {
      color: #0366d6;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .highlight {
      color: #d73a49;
    }
  </style>
</head>
<body>
  <h1>AI-Powered Resume Analyzer and Builder</h1>

  <h2>Overview</h2>
  <p>This project is an AI-powered web application designed to streamline the resume creation and analysis process for job seekers. It integrates a resume analyzer, resume builder, statistics dashboard, feedback system, and an Ollama-powered chatbot, all backed by a MySQL database. The application leverages natural language processing (NLP) and machine learning to provide actionable insights, optimize resumes for Applicant Tracking Systems (ATS), and enhance job application success.</p>

  <h2>Features</h2>
  <h3>1. Resume Analyzer</h3>
  <ul>
    <li><strong class="highlight">PDF Parsing</strong>: Extracts text from uploaded resumes in PDF format using libraries like PyPDF2.</li>
    <li><strong class="highlight">Keyword Extraction</strong>: Identifies key skills, certifications, and experiences using NLP techniques.</li>
    <li><strong class="highlight">Job Description Matching</strong>: Compares resumes against job descriptions to highlight gaps and suggest improvements.</li>
    <li><strong class="highlight">ATS Compatibility Scoring</strong>: Evaluates how well the resume aligns with ATS requirements.</li>
    <li><strong class="highlight">Skill Recommendations</strong>: Suggests additional skills to include based on job roles.</li>
  </ul>

  <h3>2. Resume Builder</h3>
  <ul>
    <li><strong class="highlight">Customizable Templates</strong>: Offers multiple professional resume templates for users to customize.</li>
    <li><strong class="highlight">Real-Time Preview</strong>: Displays resume updates in real-time as users input data.</li>
    <li><strong class="highlight">PDF Export</strong>: Allows users to download their polished resumes in PDF format.</li>
    <li><strong class="highlight">AI-Driven Suggestions</strong>: Provides content recommendations to optimize resume sections like work experience, skills, and achievements.</li>
  </ul>

  <h3>3. Statistics Data Dashboard</h3>
  <ul>
    <li><strong class="highlight">Keyword Analysis</strong>: Visualizes keyword frequency and relevance for specific job roles.</li>
    <li><strong class="highlight">Skills Gap Analysis</strong>: Displays gaps between user skills and job requirements through interactive charts.</li>
    <li><strong class="highlight">Resume Score Trends</strong>: Tracks improvements in resume scores over time.</li>
    <li><strong class="highlight">Job Match Percentage</strong>: Shows how well a resume matches various job descriptions.</li>
  </ul>

  <h3>4. Feedback System</h3>
  <ul>
    <li><strong class="highlight">Personalized Feedback</strong>: Offers detailed suggestions for improving resume content and structure.</li>
    <li><strong class="highlight">Role-Based Insights</strong>: Provides tailored advice based on the target job position.</li>
    <li><strong class="highlight">Real-Time Feedback</strong>: Updates suggestions as users modify their resumes.</li>
  </ul>

  <h3>5. Ollama Chatbot</h3>
  <ul>
    <li><strong class="highlight">AI-Powered Assistance</strong>: Powered by the Ollama framework, the chatbot provides real-time guidance for resume creation and optimization.</li>
    <li><strong class="highlight">Career Advice</strong>: Answers user queries about job applications, interview preparation, and skill development.</li>
    <li><strong class="highlight">Interactive Support</strong>: Engages with users to clarify requirements and suggest improvements.</li>
  </ul>

  <h3>6. MySQL Database</h3>
  <ul>
    <li><strong class="highlight">Data Storage</strong>: Stores user profiles, resumes, job descriptions, and analysis results.</li>
    <li><strong class="highlight">Efficient Queries</strong>: Supports fast retrieval of data for real-time dashboard updates and chatbot responses.</li>
    <li><strong class="highlight">Scalability</strong>: Handles large datasets for multiple users and job applications.</li>
  </ul>

  <h2>Tech Stack</h2>
  <ul>
    <li><strong class="highlight">Frontend</strong>: React.js, Tailwind CSS</li>
    <li><strong class="highlight">Backend</strong>: Python, FastAPI</li>
    <li><strong class="highlight">Database</strong>: MySQL</li>
    <li><strong class="highlight">AI/NLP</strong>: Ollama, Hugging Face Transformers (e.g., BERT for NER), LangChain</li>
    <li><strong class="highlight">PDF Processing</strong>: PyPDF2</li>
    <li><strong class="highlight">Dashboard</strong>: Streamlit for interactive visualizations</li>
    <li><strong class="highlight">Other Libraries</strong>: Scikit-learn, NLTK, Pandas</li>
  </ul>

  <h2>Installation</h2>
  <p>To set up and run the project locally, follow these steps:</p>
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
    <li><strong class="highlight">Clone the Repository</strong>:
      <pre><code>git clone https://github.com/Dharaneesh05/AI-powered-resume-analyzer-builder.git
cd AI-powered-resume-analyzer-builder</code></pre>
    </li>
    <li><strong class="highlight">Set Up Backend</strong>:
      <p>Install Python dependencies:</p>
      <pre><code>pip install -r requirements.txt</code></pre>
      <p>Configure MySQL:</p>
      <ul>
        <li>Create a database named <code>resume_analyzer</code>.</li>
        <li>Update database credentials in <code>config.py</code>:</li>
        <pre><code class="language-python">DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'resume_analyzer'
}</code></pre>
        <li>Run database migrations:</li>
        <pre><code>python migrate.py</code></pre>
      </ul>
    </li>
    <li><strong class="highlight">Set Up Frontend</strong>:
      <p>Navigate to the frontend directory:</p>
      <pre><code>cd frontend</code></pre>
      <p>Install dependencies:</p>
      <pre><code>npm install</code></pre>
      <p>Start the frontend server:</p>
      <pre><code>npm start</code></pre>
    </li>
    <li><strong class="highlight">Set Up Ollama</strong>:
      <ul>
        <li>Install Ollama following the official documentation: <a href="https://ollama.ai/docs/installation">Ollama Installation Guide</a>.</li>
        <li>Pull the required model (e.g., LLaMA):</li>
        <pre><code>ollama pull llama3</code></pre>
        <li>Configure the chatbot endpoint in <code>config.py</code>.</li>
      </ul>
    </li>
    <li><strong class="highlight">Run the Application</strong>:
      <p>Start the backend server:</p>
      <pre><code>uvicorn app.main:app --reload</code></pre>
      <p>Start the Streamlit dashboard:</p>
      <pre><code>streamlit run dashboard.py</code></pre>
    </li>
    <li><strong class="highlight">Access the Application</strong>:
      <ul>
        <li>Frontend: <a href="http://localhost:3000">http://localhost:3000</a></li>
        <li>Dashboard: <a href="http://localhost:8501">http://localhost:8501</a></li>
        <li>API: <a href="http://localhost:8000">http://localhost:8000</a></li>
      </ul>
    </li>
  </ol>

  <h2>ItUsage</h2>
  <ol>
    <li><strong class="highlight">Upload Resume</strong>: Upload a PDF resume or create one from scratch using the resume builder.</li>
    <li><strong class="highlight">Analyze Resume</strong>: The system extracts key information, scores ATS compatibility, and suggests improvements.</li>
    <li><strong class="highlight">View Dashboard</strong>: Check the statistics dashboard for keyword and skills gap analysis.</li>
    <li><strong class="highlight">Interact with Chatbot</strong>: Use the Ollama chatbot for real-time guidance and career advice.</li>
    <li><strong class="highlight">Export Resume</strong>: Download the optimized resume as a PDF.</li>
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
  <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

  <h2>Contact</h2>
  <p>For questions or feedback, reach out via <a href="https://github.com/Dharaneesh05/AI-powered-resume-analyzer-builder/issues">GitHub Issues</a> or email: <a href="mailto:your-email@example.com">your-email@example.com</a>.</p>

  <h2>Acknowledgments</h2>
  <ul>
    <li>Inspired by various open-source resume analysis tools.</li>
    <li>Built with love for job seekers worldwide! 🚀</li>
  </ul>
</body>
</html>
