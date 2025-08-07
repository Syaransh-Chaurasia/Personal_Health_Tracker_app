import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("EMAIL_SENDER"),
    MAIL_PASSWORD=os.getenv("EMAIL_PASSWORD"),
    MAIL_FROM=os.getenv("EMAIL_SENDER"),
    MAIL_PORT=int(os.getenv("SMTP_PORT", 587)),
    MAIL_SERVER=os.getenv("SMTP_SERVER"),
    MAIL_FROM_NAME="Your App Name",
    MAIL_STARTTLS=True,     # updated from MAIL_TLS
    MAIL_SSL_TLS=False,     # updated from MAIL_SSL
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

async def send_welcome_email(email: EmailStr, username: str):
    message = MessageSchema(
        subject="Welcome to Personal Health Tracker!",
        recipients=[email],
        body=f"Hello {username},\n\nThank you for registering with us. We're excited to have you!",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
