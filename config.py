import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
RECIPIENT = os.getenv('RECIPIENT')
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
THRESHOLD_BPM = int(os.getenv('THRESHOLD_BPM', 100))

required = {
    'EMAIL_USER': EMAIL_USER,
    'EMAIL_PASS': EMAIL_PASS,
    'RECIPIENT': RECIPIENT,
    'ENCRYPTION_KEY': ENCRYPTION_KEY,
}
for name, value in required.items():
    if not value:
        raise EnvironmentError(f"Required environment variable {name} is not set")