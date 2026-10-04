from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "jobtrack.db"

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

SEED = []

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.execute("""CREATE TABLE IF NOT EXISTS applications (
        id TEXT PRIMARY KEY, company TEXT NOT NULL, role TEXT NOT NULL,
        location TEXT, salary TEXT, status TEXT NOT NULL, date TEXT,
        url TEXT, nextAction TEXT
    )""")
    db.commit()
    db.close()

def row_dict(row):
    return dict(row)

@app.get("/api/applications")
def list_applications():
    db = get_db()
    rows = db.execute("SELECT * FROM applications ORDER BY date DESC").fetchall()
    db.close()
    return jsonify([row_dict(r) for r in rows])

@app.post("/api/applications")
def create_application():
    data = request.get_json(silent=True) or {}
    required = ["id", "company", "role", "status"]
    if any(not data.get(k) for k in required):
        return jsonify({"error": "company, role, status and id are required"}), 400
    db = get_db()
    db.execute("""INSERT INTO applications
        (id,company,role,location,salary,status,date,url,nextAction)
        VALUES (?,?,?,?,?,?,?,?,?)""",
        tuple(data.get(k, "") for k in
              ["id","company","role","location","salary","status","date","url","nextAction"]))
    db.commit()
    row = db.execute("SELECT * FROM applications WHERE id=?", (data["id"],)).fetchone()
    db.close()
    return jsonify(row_dict(row)), 201

@app.patch("/api/applications/<app_id>")
def update_application(app_id):
    data = request.get_json(silent=True) or {}
    allowed = ["company","role","location","salary","status","date","url","nextAction"]
    fields = [k for k in allowed if k in data]
    if not fields:
        return jsonify({"error": "No fields to update"}), 400
    values = [data[k] for k in fields] + [app_id]
    db = get_db()
    db.execute(f"UPDATE applications SET {', '.join(f'{k}=?' for k in fields)} WHERE id=?", values)
    db.commit()
    row = db.execute("SELECT * FROM applications WHERE id=?", (app_id,)).fetchone()
    db.close()
    if not row:
        return jsonify({"error": "Application not found"}), 404
    return jsonify(row_dict(row))

@app.post("/api/reset")
def reset_demo():
    db = get_db()
    db.execute("DELETE FROM applications")
    db.commit()
    db.close()
    return jsonify({"ok": True})

@app.get("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
