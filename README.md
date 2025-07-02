# omi-email-bot-site
# 📥 OMI Email Bot – Automated Email Intake via Flask & Mailgun

This project is built to solve [OMI’s Import Email #1895 bounty](https://github.com/orgs/BasedHardware/projects/1/views/7) by automatically receiving, parsing, and responding to inbound emails. It supports Mailgun webhook integration, logs emails in both JSONL and CSV format, and generates smart auto-replies.

---

## ✅ Features

- 📥 Receives and parses inbound emails (via Flask POST `/email`)
- 🧠 Auto-generates smart reply messages based on email intent
- 🗂️ Logs email data to:
  - `email_log.jsonl` – for structured import-ready logs
  - `emails.csv` – for human-readable backup or admin use
- 📎 Saves attachments locally
- 🔐 Mailgun-compatible for real-time email intake
- 🌐 Compatible with ngrok for public webhook forwarding

---

## 📁 File Structure

omi_email_bot/
├── app.py # Main Flask app
├── email_log.jsonl # Logs each email in JSONL format
├── emails.csv # Logs email summary and auto-reply in CSV
├── templates/ # (Optional) for HTML responses
└── README.md # You're here

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Project

```bash
git clone https://github.com/yourusername/omi-email-bot.git
cd omi-email-bot
🐍 2. Create & Activate Python Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
📦 3. Install Dependencies
bash
Copy
Edit
pip install flask requests
📬 How to Test
✅ Local Test
Run the server:

bash
Copy
Edit
python app.py
Then simulate an incoming email using curl:

bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/email ^
  -F sender="user@example.com" ^
  -F subject="Hello OMI" ^
  -F "body-plain=Can we talk about partnerships?"
🌐 Mailgun Integration
🔁 Webhook Setup (optional)
Create a Mailgun Route

Match recipient: .*

Action (Forward): https://<your-ngrok-url>/email

Priority: 0

Click "Create Route"

💡 Use ngrok http 5000 to expose your Flask app publicly.

💬 Example Auto-Reply
text
Copy
Edit
Hello user@example.com,

Thank you for your email titled 'Hello OMI'. We have received your message and will get back to you shortly.

Best regards,  
Auto-Reply Bot
🚀 Bounty Alignment
✅ Fully aligned with OMI's Import Email #1895
✅ Built with real-time routing in mind
✅ Simulates production behavior with webhook-ready JSON
✅ Open for AI-enhanced reply expansion

🧠 Future Improvements
🧾 PDF parsing of resumes, invoices, etc.

🔗 Push parsed content into OMI plugin structure

🤖 GPT-based summary or reply customization

🌍 Host on Railway/Fly.io for persistent uptime

👤 Author
Punith Chowdary Ongolu
Built this specifically for OMI Bounty – June 2025
Feel free to reach out or fork the repo!

📄 License
MIT License (Feel free to use, modify, or contribute)

vbnet
Copy
Edit

---
