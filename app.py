from flask import Flask, request, jsonify
import json
import csv
import os
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "OMI Email Bot is running!"

@app.route("/email", methods=["POST"])
def receive_email():
    sender = request.form.get("sender")
    subject = request.form.get("subject")
    body_plain = request.form.get("body-plain")
    attachments = request.files

    print("New Email Received:")
    print(f"From: {sender}")
    print(f"Subject: {subject}")
    print(f"Body: {body_plain}")

    # Smart Auto-Reply Logic
    if "support" in subject.lower() or "issue" in body_plain.lower():
        reply_message = f"Hello {sender},\n\nWe’re here to help! Please describe your issue in more detail, and our support team will get back to you.\n\nBest,\nAuto-Reply Bot"
    elif "partnership" in subject.lower() or "collaborate" in body_plain.lower():
        reply_message = f"Hello {sender},\n\nThanks for your interest in partnering with OMI! We’ve received your message and will get back to you shortly.\n\nBest,\nAuto-Reply Bot"
    else:
        reply_message = f"Hello {sender},\n\nThank you for your email titled '{subject}'. We will get back to you shortly.\n\nBest regards,\nAuto-Reply Bot"

    # Log to JSONL
    email_data = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "sender": sender,
        "subject": subject,
        "body": body_plain,
        "reply": reply_message
    }

    with open("email_log.jsonl", "a") as f:
        f.write(json.dumps(email_data) + "\n")

    # Log to CSV
    csv_file = "emails.csv"
    csv_headers = ["timestamp", "sender", "subject", "body", "reply"]
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow(email_data)

    # Save attachments
    for filename, file in attachments.items():
        file.save(f"./{filename}")
        print(f"Saved attachment: {filename}")

    print("Auto-reply message:\n" + reply_message)

    return jsonify({"status": "received", "auto_reply": reply_message}), 200

if __name__ == "__main__":
    app.run(port=5000)
