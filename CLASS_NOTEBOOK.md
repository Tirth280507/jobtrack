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
- localStorage persistence so the MVP works without a backend.
- Insights and next-action views.

### Why no backend yet?
The first version should validate the workflow and remain easy to deploy. A backend can be added after the core experience proves useful.

### Reflection
The project evolved from a generic productivity concept into a job-search tool because it has a clearer real-world use case and a stronger interview story.

### Future ideas
Authentication, cloud sync, reminders, calendar/email integrations, CSV export, and richer analytics.