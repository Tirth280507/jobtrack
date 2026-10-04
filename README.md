# JobTrack

**JobTrack** is a full-stack job-application manager built with a polished HTML/CSS/JavaScript frontend and a Python/Flask backend.

### Why it exists
Job searches often get scattered across spreadsheets, browser tabs, email, and notes. JobTrack gives the search one focused workspace: pipeline, next actions, and simple progress signals.

### Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python + Flask REST API
- **Database:** SQLite
- **Production server:** Gunicorn
- **Deployment:** Render

### Features
- Dashboard with active applications, interviews, offers, and response rate
- Six-stage application pipeline
- Add applications through a structured form
- Search and filter applications
- Change an application's stage directly from the pipeline
- Next-action / follow-up view
- Simple insights page
- Persistent database storage
- Responsive layout

### API
- `GET /api/applications` — list applications
- `POST /api/applications` — create an application
- `PATCH /api/applications/<id>` — update an application
- `POST /api/reset` — reset demo data

### Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000`.

### Deployment
The repository includes `render.yaml` for Render. Render's Python web service can build with `pip install -r requirements.txt` and run with `gunicorn app:app`.

### Class Notebook
See `CLASS_NOTEBOOK.md`.
