# backend/utils/email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_welcome_email(to_email: str):
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")

    subject = "Welcome to My Health Tracker App!"
    body = f"""\
Hi there 👋,

Welcome to My Health Tracker App! 🎉
We're excited to have you on board. Start tracking your health today.

Best regards,  
The MyHealthTracker Team
"""

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
    except Exception as e:
        print(f"❌ Error sending email: {e}")
