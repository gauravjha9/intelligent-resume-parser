# intelligent-resume-parser

This is a simple web app that reads resumes (PDF or DOCX) and gives a clean, structured JSON output with all important details like name, email, phone, skills, work experience, education, etc.

It uses:
- ⚙️ FastAPI for the backend
- 🤖 OpenAI (via LangChain) to extract structured data
- 🎨 HTML + Tailwind CSS for a basic frontend UI

---

## Features

- Upload a resume file (`.pdf` or `.docx`)
- Extracts:
  - Name, Email, Phone
  - LinkedIn, GitHub
  - Summary, Skills
  - Work Experience
  - Projects & Education
- Returns minified, readable JSON
- Works locally on your machine

---

## How to Run

### 1. Clone the Project

```bash
git clone https://github.com/your-username/intelligent-resume-parser.git
cd intelligent-resume-parser
```

### 2. Backend setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt 
```

### 3. Setup .env file

- APP_NAME="Intelligent Resume Parser"
- APP_ENV=development
- APP_DEBUG=True
- APP_VERSION=1.0.0
- API_VERSION=v1

- GROQ_API_KEY=<your-api-key>


### 4. Start FastAPI Server
```bash
fastapi dev
```

### 5. Frontend
1. Open frontend/index.html in your browser.
2. Choose a resume file (PDF or DOCX).
3. Click upload.
4. JSON response will appear below.
