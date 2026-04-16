# Real-time-alert-

A backend service to monitor data streams, detect anomalies (e.g., high BPM), and push encrypted notifications.

## Setup

1. Install dependencies: `pip install -r requirements.txt`

2. Copy `.env.example` to `.env` and fill in your values.

3. Generate encryption key: `python generate_key.py` and set it in `.env`

4. Run the service: `python app.py`

## Environment Variables

- EMAIL_HOST: SMTP host (default: smtp.gmail.com)
- EMAIL_PORT: SMTP port (default: 587)
- EMAIL_USER: Your email
- EMAIL_PASS: Your email password (use app password for Gmail)
- RECIPIENT: Email to send notifications to
- ENCRYPTION_KEY: Generated Fernet key
- THRESHOLD_BPM: BPM threshold for anomaly (default: 100)

## Features

- Simulates BPM data stream
- Detects anomalies when BPM exceeds threshold
- Encrypts alert messages
- Sends encrypted notifications via email