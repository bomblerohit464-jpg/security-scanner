
from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/<path:filename>")
def website_files(filename):
    if filename in ("style.css", "script.js"):
        return send_from_directory(BASE_DIR, filename)
    return "Not found", 404


@app.route("/api/results")
def results():
    bandit_file = os.path.join(BASE_DIR, "bandit-report.json")
    audit_file = os.path.join(BASE_DIR, "dependency-report.json")

    if not os.path.exists(bandit_file) or not os.path.exists(audit_file):
        return jsonify({
            "status": "WAITING",
            "checks": 0,
            "issues": "--",
            "message": "Run the Jenkins security pipeline first."
        }), 503

    with open(bandit_file, encoding="utf-8") as file:
        bandit = json.load(file)

    with open(audit_file, encoding="utf-8") as file:
        audit = json.load(file)

    bandit_issues = len(bandit.get("results", []))
    dependency_issues = len(audit) if isinstance(audit, list) else 0
    total = bandit_issues + dependency_issues

    return jsonify({
        "status": "REVIEW" if total else "PASS",
        "checks": 2,
        "issues": total,
        "message": "Scan reports loaded. Review findings before deployment."
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
