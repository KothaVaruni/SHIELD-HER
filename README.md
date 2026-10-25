# 🛡️ SHIELD HER — Women's Safety Web Application

> **"Your Safety. Your Power."**  
> *Developed for the **recHERsion'26** Women-Only Hackathon.*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![pytest](https://img.shields.io/badge/pytest-31%20Passed-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

## 🌟 1. Project Overview

**SHIELD HER** is a functional, multi-page women's safety ecosystem created to provide actionable personal defense, travel monitoring, and digital evidence security in one private web interface.

Built by a second-year B.Tech CSE student, the platform focuses on solving real-world challenges faced by women commuters, college students, and internet users without false promises, privacy violations, or covert tracking.

### 🎯 Key Safety Pillars

1. **🚨 Emergency SOS Hub (`/sos`):**
   - Assemble high-priority emergency messages with one click.
   - Attach browser-approved GPS coordinates (`https://maps.google.com/?q=lat,lng`) with explicit user consent.
   - Instant dispatch options: **WhatsApp Direct Share**, **Native SMS App Protocol**, **Web Share API**, and **One-Click Clipboard Copy**.
   - Optional server-side automated SMS dispatch via **Twilio** with honest reporting (no fake "SMS Sent" messages when unconfigured).

2. **🧭 Safe Journey Planner (`/journeys`):**
   - Plan commutes, evening cab rides, and transit routes with departure and expected arrival deadlines.
   - Assign a designated trusted contact/guardian to monitor the journey.
   - Record milestone safety check-ins (e.g., "Boarded cab UP16-AB-1234", "Passed metro gate").
   - Automatically detects and flags **Overdue Arrivals**.

3. **🛡️ CyberShield Incident Vault (`/incidents`):**
   - Document cyberbullying, stalking, predatory DMs, and online fraud before attackers delete messages.
   - Securely upload supporting screenshots and media files outside the public web root.
   - Generates **SHA-256 cryptographic hashes** for digital chain-of-custody verification (compliant with Indian Evidence Act / Section 65B requirements).
   - Strict server-side ownership checks prevent cross-user file access.

4. **👥 Trusted Contacts Network (`/contacts`):**
   - Manage primary emergency contacts, family members, mentors, and roommates.
   - Server-enforced ownership checks prevent any other user from viewing or tampering with contacts.

5. **📚 Safety Resource Center (`/resources`):**
   - Searchable, categorized repository of verified national emergency helplines in India (**112**, **1091**, **1930**, **181**, **1098**).
   - Practical guidelines for evidence preservation, reporting cyber abuse on `cybercrime.gov.in`, and legal rights in India (Zero FIR).

6. **🔒 Privacy & Data Sovereignty (`/privacy`):**
   - GDPR-compliant **JSON Data Export** for full data portability.
   - Permanent account deletion with physical file purging from disk.
   - Zero background GPS tracking—coordinates are requested only with active user permission.

---

## 🏗️ 2. Technology Stack & Architecture

- **Backend:** Python 3.11+ / 3.14, Flask application factory pattern with modular Blueprints.
- **ORM & Database:** SQLAlchemy & Flask-SQLAlchemy with SQLite (development) and PostgreSQL compatibility (production).
- **Authentication:** Flask-Login with secure session cookies (`HttpOnly`, `SameSite=Lax`).
- **Security & Forms:** Flask-WTF with CSRF protection and Werkzeug secure password hashing (`scrypt`).
- **Frontend:** Responsive HTML5, modern CSS3 design system (Deep Navy `#0A1128`, Purple `#7B2CBF`, Pink Accent `#F72585`), JavaScript ES6, and Jinja2 templates.
- **Testing:** pytest automated test suite with in-memory isolated database.

---

## 🚀 3. Windows Setup & Running Instructions

Follow these step-by-step instructions in Windows PowerShell to set up and run the application on your laptop.

### Step 1: Open the Project in VS Code
1. Open **Visual Studio Code**.
2. Click **File > Open Folder...** and select `Shield-Her`.
3. Open the built-in terminal by pressing `` Ctrl + ` `` (backtick).

### Step 2: Create a Python Virtual Environment
In the PowerShell terminal, run:
```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```
> *Tip:* If you encounter an execution policy restriction in PowerShell, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once, or activate via `.\venv\Scripts\activate.bat` in Command Prompt.

When activated, you will see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables
Copy `.env.example` to create your local `.env` file:
```powershell
Copy-Item .env.example .env
```
*(The default settings in `.env` are pre-configured to run out of the box with zero external setup.)*

### Step 6: Populate Demo Data (Optional for Hackathon Presentation)
We have included a seed script that automatically creates a demo user, trusted contacts, an active journey with check-ins, and a cyberbullying report:
```powershell
python seed.py
```
> **Demo Credentials:**
> - **Email:** `demo@shieldher.local`
> - **Password:** `ShieldHer2026!`

### Step 7: Start the Flask Server
```powershell
python run.py
```

### Step 8: Open in Your Browser
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

### Step 9: How to Stop and Restart the Server
- **To stop:** Press `Ctrl + C` in the terminal.
- **To restart:** Run `python run.py` again.

---

## 🧪 4. Automated Testing & Verification

Run the full pytest suite to verify all routes, authorization checks, and data isolation:

```powershell
python -m pytest -v
```

### Actual Test Suite Results:
```text
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-8.4.2 -- tests/
collected 31 items

tests/test_auth.py::test_landing_page PASSED                             [  3%]
tests/test_auth.py::test_user_registration_success PASSED                [  6%]
tests/test_auth.py::test_duplicate_email_registration_fails PASSED       [  9%]
tests/test_auth.py::test_password_length_validation PASSED               [ 12%]
tests/test_auth.py::test_login_valid_credentials PASSED                  [ 16%]
tests/test_auth.py::test_login_invalid_password PASSED                   [ 19%]
tests/test_auth.py::test_logout PASSED                                   [ 22%]
tests/test_auth.py::test_protected_pages_require_auth PASSED             [ 25%]
tests/test_auth.py::test_password_reset_token_workflow PASSED            [ 29%]
tests/test_auth.py::test_profile_update PASSED                           [ 32%]
tests/test_auth.py::test_personal_data_export PASSED                     [ 35%]
tests/test_auth.py::test_account_deletion_with_confirmation PASSED       [ 38%]
tests/test_contacts.py::test_add_trusted_contact PASSED                  [ 41%]
tests/test_contacts.py::test_edit_trusted_contact PASSED                 [ 45%]
tests/test_contacts.py::test_delete_trusted_contact PASSED               [ 48%]
tests/test_incidents.py::test_create_incident_without_attachment PASSED  [ 51%]
tests/test_incidents.py::test_create_incident_with_evidence_file PASSED  [ 54%]
tests/test_incidents.py::test_disallowed_file_extension_rejected PASSED  [ 58%]
tests/test_incidents.py::test_download_evidence_file PASSED              [ 61%]
tests/test_incidents.py::test_delete_incident_purges_evidence PASSED     [ 64%]
tests/test_isolation.py::test_contact_isolation PASSED                   [ 67%]
tests/test_isolation.py::test_journey_isolation PASSED                   [ 70%]
tests/test_isolation.py::test_incident_and_evidence_isolation PASSED     [ 74%]
tests/test_isolation.py::test_dashboard_data_isolation PASSED            [ 77%]
tests/test_journeys.py::test_create_safe_journey PASSED                  [ 80%]
tests/test_journeys.py::test_record_manual_checkin PASSED                [ 83%]
tests/test_journeys.py::test_mark_journey_arrived PASSED                 [ 87%]
tests/test_journeys.py::test_cancel_journey PASSED                       [ 90%]
tests/test_sos_and_resources.py::test_sos_hub_renders_with_contacts PASSED [ 93%]
tests/test_sos_and_resources.py::test_sos_sms_honest_reporting_when_unconfigured PASSED [ 96%]
tests/test_sos_and_resources.py::test_safety_resource_center_verified_helplines PASSED [100%]

============================= 31 passed in 8.67s ==============================
```

---

## 📁 5. Project Directory Structure

```
Shield-Her/
├── .env.example              # Environment variables template
├── .gitignore                # Git exclusions (uploads, instance, venv, secrets)
├── config.py                 # Configuration classes (Dev, Test, Prod)
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
├── seed.py                   # Demo database seeder for hackathon pitch
├── README.md                 # Project guide & Windows instructions
├── app/
│   ├── __init__.py           # Application factory (create_app)
│   ├── extensions.py         # SQLAlchemy, LoginManager, CSRFProtect
│   ├── models.py             # Database models (User, Contact, Journey, etc.)
│   ├── auth/                 # Authentication & Account Blueprint
│   │   ├── forms.py
│   │   └── routes.py         # /login, /register, /profile, /privacy
│   ├── contacts/             # Trusted Contacts Blueprint
│   │   ├── forms.py
│   │   └── routes.py         # /contacts, /contacts/<id>/edit, delete
│   ├── journeys/             # Safe Journey Blueprint
│   │   ├── forms.py
│   │   └── routes.py         # /journeys, /journeys/new, /check-in
│   ├── incidents/            # CyberShield Incident Vault Blueprint
│   │   ├── forms.py
│   │   ├── routes.py         # /incidents, /incidents/new, evidence serving
│   │   └── utils.py          # Secure file saving, MIME validation & SHA-256
│   ├── main/                 # Core Pages Blueprint
│   │   └── routes.py         # /, /dashboard, /resources
│   ├── sos/                  # Emergency SOS Blueprint
│   │   ├── forms.py
│   │   └── routes.py         # /sos, message assembly & Twilio client
│   ├── static/
│   │   ├── css/style.css     # Responsive design system
│   │   ├── js/main.js        # Mobile menu, GPS toggle, WhatsApp/Clipboard
│   │   └── img/logo.svg      # Shield emblem SVG logo
│   └── templates/            # Jinja2 templates for all individual pages
│       ├── base.html         # Base template with responsive navbar & footer
│       ├── errors/           # 400, 403, 404, 413, 500 error templates
│       ├── auth/             # Login, register, profile, privacy templates
│       ├── contacts/         # Trusted contact management templates
│       ├── incidents/        # Incident vault, dossier & edit templates
│       ├── journeys/         # Journey index, planner & live tracker
│       ├── main/             # Landing, dashboard & resources templates
│       └── sos/              # Interactive Emergency SOS console
├── instance/                 # Local SQLite database (excluded from Git)
├── uploads/                  # Private evidence storage (excluded from Git)
└── tests/                    # 31 automated pytest tests
    ├── conftest.py
    ├── test_auth.py
    ├── test_contacts.py
    ├── test_incidents.py
    ├── test_isolation.py     # Cross-user authorization checks
    ├── test_journeys.py
    └── test_sos_and_resources.py
```

---

## 🔒 6. Security & Privacy Commitments

1. **Private Evidence Storage:** Uploaded files are stored in a private directory located outside the web root (`uploads/`). They are renamed with secure random UUIDs to eliminate path-traversal vulnerabilities.
2. **Access Control (Authorization):** Serving an evidence file requires both authentication and an explicit database check (`evidence.user_id == current_user.id`). Unauthorized access immediately returns `403 Forbidden`.
3. **Forensic Integrity:** Uploads are hashed with **SHA-256** at the moment of intake, recording an immutable cryptographic fingerprint.
4. **No Covert GPS Tracking:** SHIELD HER never silently queries or tracks the user's location. GPS coordinates are acquired strictly inside the browser when the user explicitly checks the box.
5. **No Fake SMS Promises:** When Twilio is unconfigured, the system explicitly reports that automated SMS dispatch is in local development mode, steering the user to WhatsApp, device SMS, or clipboard sharing.

---

## 🌐 7. Production Deployment Guide

To deploy SHIELD HER to a cloud provider (Render, Railway, Fly.io, or an Ubuntu VPS):

1. **Production Server:** Use a WSGI HTTP server such as `gunicorn`:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```
2. **Database:** Switch from SQLite to PostgreSQL by updating `DATABASE_URL` in `.env`:
   ```env
   DATABASE_URL=postgresql://user:password@host:5432/shield_her_db
   ```
3. **Persistent Volume:** Ensure the `UPLOAD_FOLDER` directory is mounted on a persistent disk or cloud storage bucket (AWS S3) so uploaded evidence persists across server redeployments.
4. **HTTPS Enforced:** Enable `SESSION_COOKIE_SECURE = True` and terminate SSL/TLS at your reverse proxy (Nginx or Cloudflare).
5. **Optional Twilio Setup:**
   - Sign up at [Twilio](https://www.twilio.com/).
   - Obtain `Account SID`, `Auth Token`, and a virtual phone number.
   - Add them to `.env`:
     ```env
     TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
     TWILIO_AUTH_TOKEN=your_auth_token_here
     TWILIO_PHONE_NUMBER=+1234567890
     ```

---

## 🎤 8. Hackathon Pitch & Demonstration Guide

When presenting to hackathon judges:

1. **The Problem:** Women face both physical transit vulnerabilities and rampant online harassment/cyberbullying. Existing solutions either require expensive hardware, constantly drain battery with background GPS tracking, or offer fake prototype buttons.
2. **The Solution:** A unified, multi-page platform with separate functional modules:
   - *Emergency SOS:* Fast dispatch via WhatsApp and SMS without requiring paid APIs.
   - *Safe Journey:* Accountability during late-night commutes with milestone check-ins.
   - *CyberShield:* Verifiable forensic preservation of online abuse with SHA-256 digital integrity.
   - *Data Sovereignty:* Full user ownership with GDPR-compliant JSON data export.
3. **Live Demonstration Flow:**
   - Open `http://127.0.0.1:5000` (show landing page and design).
   - Log in using `demo@shieldher.local` / `ShieldHer2026!`.
   - Show real database statistics on the personalized Dashboard.
   - Open **Emergency SOS**: Toggle GPS permission, preview live formatted message, click "Copy Message" or "Open WhatsApp".
   - Open **Safe Journey**: Demonstrate active trip to campus, add a milestone check-in, mark arrived.
   - Open **CyberShield**: View documented harassment report, explain private evidence file handling and SHA-256 integrity hash.
   - Open **Privacy Center**: Click "Export My Data (JSON)" to showcase data portability.
   - Run `python -m pytest` in terminal to prove 31 passing unit tests and cross-user data isolation.

---

## 📄 License & Disclaimer

- **License:** MIT License. Built for educational and hackathon evaluation purposes.
- **Disclaimer:** SHIELD HER is an empowerment and communication tool. It does not replace the police or emergency services. In life-threatening emergencies, dial **112** (India) or your local emergency hotline immediately.
