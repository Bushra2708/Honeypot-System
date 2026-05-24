# Honeypot System – Cyber Threat Intelligence & SOC Monitoring Platform

## Description

Honeypot System is a modern cybersecurity monitoring platform built using Flask and SQLAlchemy that simulates a vulnerable enterprise login portal to capture and analyze intrusion attempts in real time. The project is designed with a professional SOC (Security Operations Center) interface featuring live telemetry feeds, attack analytics, credential tracking, GeoIP intelligence, browser fingerprinting, and real-time monitoring dashboards.

The system records attacker activity such as usernames, passwords, IP addresses, operating systems, browsers, and referrers while presenting the data through a visually rich SIEM-style dashboard. The project supports deployment on Render with PostgreSQL integration, environment-based configuration, and secure admin authentication.

---

# Features

* Fake enterprise login honeypot
* Real-time attack telemetry
* SOC-style monitoring dashboard
* Credential harvesting simulation
* GeoIP and IP intelligence
* Browser and device fingerprinting
* Live dashboard auto-refresh
* Search and pagination system
* Expandable attack forensic logs
* Admin authentication system
* PostgreSQL deployment support
* Proxy-aware IP tracking
* JSON telemetry API endpoint
* Modern cyber-themed UI

---

# Technologies Used

## Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Gunicorn

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js
* Lucide Icons

## Database

* SQLite (Local Development)
* PostgreSQL (Production Deployment)

## Deployment

* Render
* GitHub

---

# Project Structure

```plaintext id="z6k2qx"
honeypot-system/
│
├── app/
│   ├── models/
│   │   ├── attack.py
│   │   └── admin.py
│   │
│   ├── routes/
│   │   └── main_routes.py
│   │
│   ├── templates/
│   │   ├── honeypot/
│   │   │   ├── login.html
│   │   │   └── failure.html
│   │   │
│   │   └── dashboard/
│   │       ├── dashboard.html
│   │       └── admin_login.html
│   │
│   ├── utils/
│   │   └── tracker.py
│   │
│   └── __init__.py
│
├── instance/
│   └── honeypot.db
│
├── config.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── run.py
└── README.md
```

---

# Installation & Local Setup

## 1. Clone Repository

```bash id="h8v1mp"
git clone https://github.com/yourusername/honeypot-system.git
```

---

## 2. Navigate Into Project

```bash id="t3m7qx"
cd honeypot-system
```

---

## 3. Create Virtual Environment

```bash id="k5x2rv"
python -m venv venv
```

---

## 4. Activate Virtual Environment

### PowerShell

```bash id="f1n8wy"
.\venv\Scripts\Activate
```

### CMD

```bash id="g4m9tk"
venv\Scripts\activate.bat
```

---

## 5. Install Dependencies

```bash id="r2v6xp"
pip install -r requirements.txt
```

---

## 6. Run Application

```bash id="w7m3qn"
python run.py
```

---

# Local URLs

## Public Honeypot Portal

```plaintext id="y9k1rv"
http://127.0.0.1:5000/
```

---

## Admin Dashboard Login

```plaintext id="b5x7mq"
http://127.0.0.1:5000/dashboard-access
```

---

# Admin Credentials

Configured using environment variables:

```plaintext id="u4m8zp"
ADMIN_USERNAME
ADMIN_PASSWORD
```

Fallback example:

```plaintext id="p1v5tw"
Username: admin
Password: secure123
```

---

# API Endpoint

## Attack Telemetry API

```plaintext id="x8m2qr"
/api/attacks
```

Returns JSON-based attack logs for live dashboard streaming.

---

# Environment Variables

## Required for Production

```plaintext id="m6x4ky"
SECRET_KEY
ADMIN_USERNAME
ADMIN_PASSWORD
DATABASE_URL
```

---

# Deployment on Render

## Build Command

```plaintext id="c9v1rt"
pip install -r requirements.txt
```

---

## Start Command

```plaintext id="n2m8qx"
gunicorn run:app
```

---

# Procfile

```plaintext id="q7x3mv"
web: gunicorn run:app
```

---

# runtime.txt

```plaintext id="k1v9wr"
python-3.11.9
```

---

# Inputs Captured

* Username attempts
* Password attempts
* IP address
* Browser type
* Operating system
* Device information
* Referrer source
* Organization data
* Country and city
* User-agent strings

---

# Outputs Generated

* Real-time telemetry feed
* Attack analytics dashboard
* Credential targeting trends
* Country attack statistics
* Browser/device analysis
* Threat monitoring logs

---

# Security Notes

This project is designed strictly for:

* cybersecurity education
* ethical security research
* portfolio demonstrations
* attack simulation environments

Do not deploy this system in unauthorized production environments for malicious purposes.

---

# Live Deployment

## Public Portal
https://honeypot-system-5w4t.onrender.com/

---

## Protected Dashboard
https://honeypot-system-5w4t.onrender.com/dashboard

