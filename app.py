from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText
import asyncio
import random
import config

async def monitor_stream():
    while True:
        bpm = random.randint(60, 120)  # simulate BPM data
        print(f"Current BPM: {bpm}")
        if bpm > config.THRESHOLD_BPM:
            message = f"Anomaly detected: BPM {bpm} is high!"
            encrypted_msg = encrypt_message(message)
            await send_notification(encrypted_msg)
        await asyncio.sleep(1)  # poll every second

def encrypt_message(message):
    if not config.ENCRYPTION_KEY:
        raise ValueError("ENCRYPTION_KEY not set")
    f = Fernet(config.ENCRYPTION_KEY.encode())
    return f.encrypt(message.encode()).decode()

async def send_notification(encrypted_msg):
    msg = MIMEText(encrypted_msg)
    msg['Subject'] = 'Encrypted Alert'
    msg['From'] = config.EMAIL_USER
    msg['To'] = config.RECIPIENT

    try:
        server = smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_PORT)
        server.starttls()
        server.login(config.EMAIL_USER, config.EMAIL_PASS)
        server.sendmail(config.EMAIL_USER, config.RECIPIENT, msg.as_string())
        server.quit()
        print("Notification sent")
    except Exception as e:
        print(f"Failed to send: {e}")

if __name__ == "__main__":
    asyncio.run(monitor_stream())