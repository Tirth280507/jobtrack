# Class Notebook — JobTrack

## Entry 01 — 2026-10-04

### Goal
Turn the deployment assignment into a useful portfolio project rather than a toy demo.

### Problem
Job searches can become fragmented across spreadsheets, notes, email, and browser tabs. JobTrack puts applications, stages, follow-ups, and basic signals into one focused workspace.

### MVP decisions
- Six pipeline stages: Saved, Applied, Screening, Interview, Offer, Rejected.
- Dashboard metrics for active applications, interviews, offers, and response rate.
- Structured application form.
- Search and stage filtering.
- Direct stage changes in the Kanban board.
- Flask backend with a REST API.
- SQLite database for persistent application data.
- Insights and next-action views.

### Why add a backend?
The first visual prototype used browser storage to validate the workflow. The project then evolved into a full-stack version so application data could be handled by a Python/Flask backend and stored in SQLite.

### Reflection
The project evolved from a generic productivity concept into a job-search tool because it has a clearer real-world use case and a stronger interview story.

### Deployment
The application is hosted on Render and the source code is maintained in GitHub. Deployment makes the app accessible through a public web URL instead of only running on the developer’s computer.

### Future ideas
Authentication, cloud sync, reminders, calendar/email integrations, CSV export, and richer analytics.