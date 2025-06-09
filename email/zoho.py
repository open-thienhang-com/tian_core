import aiosmtplib
from email.message import EmailMessage
import os

SMTP_HOST = "smtp.zoho.com"
SMTP_PORT = 587
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "test@thienhang.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your_password_here")

SENDER_NAME = os.getenv("APP_NAME", "api.thienhang.com")
SENDER_EMAIL = SMTP_USERNAME

async def send_email(to: str, subject: str, content: str):
    message = EmailMessage()
    message["From"] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
    message["To"] = to
    message["Subject"] = subject
    message.set_content(content, subtype="html")

    try:
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            start_tls=True,
            username=SMTP_USERNAME,
            password=SMTP_PASSWORD,
        )
        print(f"✅ Email OTP sent to {to}")
    except Exception as e:
        print(f"❌ Failed to send email OTP to {to}: {e}")
        raise