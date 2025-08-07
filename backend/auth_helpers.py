import smtplib
from email.mime.text import MIMEText
import os

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

def send_welcome_email(email: str, name: str):
    subject = "Welcome to Personal Health Tracker"
    body = f"Hi {name},\n\nWelcome to the Personal Health Tracker App!\n\nWe're excited to have you on board.\n\nStay healthy!"
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = EMAIL_SENDER
    message["To"] = email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, email, message.as_string())
    except Exception as e:
        print(f"Error sending welcome email: {e}")
