# JobTrack

> **A focused command center for managing a job search.**

JobTrack is a full-stack web application that helps job seekers keep applications, interview stages, salary information, application dates, job links, and next actions in one place.

Instead of managing a job search across spreadsheets, browser tabs, notes, and emails, JobTrack provides one simple workspace.

## 🚀 Live App

**Live application:** https://jobtrack-1-kqju.onrender.com


## ✨ What JobTrack Does

### Dashboard
- Active applications
- Interviews
- Offers
- Response rate
- Pipeline progress
- Next actions
- Recent applications

### Applications Workspace
- Add a new job application
- Search and filter applications
- See salary and application date at a glance
- Select an application to view its full details
- Open the original job posting
- Change the application stage
- See the next action for each opportunity

### Pipeline
Applications move through six stages:

**Saved → Applied → Screening → Interview → Offer / Rejected**

### Insights
A simple overview of application activity and follow-ups helps show where the search is building momentum.

## 🛠️ Technology

| Part | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| API | REST-style HTTP endpoints |
| Database | SQLite |
| Production server | Gunicorn |
| Version control | GitHub |
| Deployment | Render |

## 🏗️ How It Works

```text
                 USER
                   │
                   ▼
        ┌─────────────────────┐
        │     Frontend        │
        │ HTML + CSS + JS     │
        └──────────┬──────────┘
                   │
                API requests
                   │
                   ▼
        ┌─────────────────────┐
        │       Flask         │
        │   Python backend    │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │       SQLite        │
        │      Database       │
        └─────────────────────┘
```

When a user adds an application, JavaScript sends the information to the Flask API, Flask stores it in SQLite, and the frontend loads the updated data.

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/applications` | Get all applications |
| POST | `/api/applications` | Create an application |
| PATCH | `/api/applications/<id>` | Update an application |
| POST | `/api/reset` | Clear stored applications |

## 💻 Run JobTrack Locally

### 1. Clone the repository

```bash
git clone https://github.com/Tirth280507/jobtrack.git
cd jobtrack
```

### 2. Create a virtual environment

**Windows**
```bash
python -m venv .venv
.venv\\Scripts\\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open `http://localhost:5000`.

## 📁 Project Structure

```text
jobtrack/
├── app.py
├── app.js
├── index.html
├── style.css
├── requirements.txt
├── Dockerfile
├── Procfile
├── render.yaml
├── .python-version
├── CLASS_NOTEBOOK.md
├── README.md
└── .gitignore
```

## 📚 What I Learned

This project helped me understand how a real web application is put together.

Key concepts explored:

- Responsive frontend development
- JavaScript application interactions
- Python and Flask backend development
- API endpoints and frontend/backend communication
- SQLite data storage
- GitHub version control
- Cloud deployment
- Connecting a deployed frontend and backend
- Designing software around a real user problem

## 🔮 Future Improvements

- User accounts and authentication
- PostgreSQL for production-scale storage
- Recruiter/contact information
- Interview dates and notes
- Application activity timeline
- Reminders and notifications
- Calendar and email integrations
- CSV export
- Richer analytics

## 📝 Development Log

See **[CLASS_NOTEBOOK.md](CLASS_NOTEBOOK.md)** for the development process, decisions, and reflections.

## 👤 Project

Built as a learning and portfolio project focused on solving a real-world job-search problem.
