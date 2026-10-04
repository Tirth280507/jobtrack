from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os
from pathlib import Path
from uuid import uuid4

app = Flask(__name__)
CORS(app)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("JOBTRACK_DB", BASE_DIR / "jobtrack.db"))

SEED = [
    ("1","Siemens","Product Analyst","Munich · Hybrid","€60k–€72k","Interview","2026-09-29","https://siemens.com","Prepare case study"),
    ("2","Zalando","Junior Product Manager","Berlin · Hybrid","€55k–€68k","Applied","2026-10-01","https://zalando.com","Follow up Oct 8"),
    ("3","Celonis","Business Analyst","Munich · Hybrid","€58k–€70k","Screening","2026-10-02","https://celonis.com","Send availability"),
    ("4","SAP","Associate Consultant","Walldorf · Hybrid","€52k–€65k","Saved","2026-10-03","https://sap.com","Tailor CV"),
    ("5","Delivery Hero","Operations Associate","Berlin · Hybrid","€48k–€58k","Rejected","2026-09-24","https://deliveryhero.com","Review feedback"),
]

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id TEXT PRIMARY KEY,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            location TEXT DEFAULT '',
            salary TEXT DEFAULT '',
            status TEXT NOT NULL,
            date TEXT NOT NULL,
            url TEXT DEFAULT '',
            nextAction TEXT DEFAULT ''
        )
        """)
        if db.execute("SELECT COUNT(*) FROM applications").fetchone()[0] == 0:
            db.executemany(
                "INSERT INTO applications VALUES (?,?,?,?,?,?,?,?,?)", SEED
            )
        db.commit()

def row_to_dict(row):
    return dict(row)

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "JobTrack API"}

@app.get("/api/applications")
def list_applications():
    with get_db() as db:
        rows = db.execute("SELECT * FROM applications ORDER BY date DESC").fetchall()
    return jsonify([row_to_dict(r) for r in rows])

@app.post("/api/applications")
def create_application():
    data = request.get_json(silent=True) or {}
    required = ["company", "role", "status", "date"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    application = {
        "id": str(uuid4()),
        "company": data["company"].strip(),
        "role": data["role"].strip(),
        "location": data.get("location", "").strip(),
        "salary": data.get("salary", "").strip(),
        "status": data["status"],
        "date": data["date"],
        "url": data.get("url", "").strip(),
        "nextAction": data.get("nextAction", "").strip(),
    }
    with get_db() as db:
        db.execute(
            "INSERT INTO applications VALUES (:id,:company,:role,:location,:salary,:status,:date,:url,:nextAction)",
            application,
        )
        db.commit()
    return jsonify(application), 201

@app.patch("/api/applications/<application_id>")
def update_application(application_id):
    data = request.get_json(silent=True) or {}
    allowed = {"company","role","location","salary","status","date","url","nextAction"}
    updates = {k: v for k, v in data.items() if k in allowed}
    if not updates:
        return jsonify({"error": "No valid fields supplied"}), 400

    assignments = ", ".join(f"{key} = ?" for key in updates)
    values = list(updates.values()) + [application_id]
    with get_db() as db:
        cursor = db.execute(
            f"UPDATE applications SET {assignments} WHERE id = ?", values
        )
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Application not found"}), 404
        row = db.execute(
            "SELECT * FROM applications WHERE id = ?", (application_id,)
        ).fetchone()
    return jsonify(row_to_dict(row))

@app.delete("/api/applications/<application_id>")
def delete_application(application_id):
    with get_db() as db:
        cursor = db.execute("DELETE FROM applications WHERE id = ?", (application_id,))
        db.commit()
    if cursor.rowcount == 0:
        return jsonify({"error": "Application not found"}), 404
    return "", 204

@app.post("/api/reset")
def reset_demo():
    with get_db() as db:
        db.execute("DELETE FROM applications")
        db.executemany("INSERT INTO applications VALUES (?,?,?,?,?,?,?,?,?)", SEED)
        db.commit()
    return jsonify({"status": "reset"})

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
