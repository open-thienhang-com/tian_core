import os
import smtplib
from email.message import EmailMessage
from string import Template
from tian_core.logger import logger
from .zoho import send_email as send_email_by_zoho

# --- Functional Version ---

def get_template_dir(custom_dir=""):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

def load_templates(template_dir):
    templates = {}
    for filename in os.listdir(template_dir):
        if filename.endswith('.html'):
            logger.info(f"Loading template: {filename}")
            with open(os.path.join(template_dir, filename), 'r', encoding='utf-8') as f:
                templates[filename] = Template(f.read())
    return templates

def get_template_content(templates, template_name, data: dict[str, str] = None):
    template = templates.get(template_name)
    if not template:
        raise ValueError(f"Template '{template_name}' not found.")
    print(data)
    return template.safe_substitute(data or {})

async def send_email(template_content, to_email, subject, smtp_server, smtp_port, smtp_user, smtp_pass):
    msg = EmailMessage()
    msg.set_content(template_content, subtype='html')
    msg['Subject'] = subject
    msg['From'] = "open@thienhang.com"
    msg['To'] = to_email

    # with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    #     server.login(smtp_user, smtp_pass)
    #     server.send_message(msg)
    try:
        await send_email_by_zoho(
            to=to_email,
            subject=subject,
            content=template_content,
            # smtp_server=smtp_server,
            # smtp_port=smtp_port,
            # smtp_user=smtp_user,
            # smtp_pass=smtp_pass
        )
        
    except Exception as e:
        print(f"❌ Failed to send email OTP to {to_email}: {e}")
        raise

# --- Composable Functional Wrappers ---

async def prepare_and_send_email(template_name, data, to_email, subject, smtp_user, smtp_pass):
    template_dir = get_template_dir(os.path.join(os.getcwd(), "templates/email"))
    templates = load_templates(template_dir)
    content = get_template_content(templates, template_name, data)

    await send_email(
        template_content=content,
        to_email=to_email,
        subject=subject,
        smtp_server="smtp.sendgrid.net",
        smtp_port=465,
        smtp_user=smtp_user,
        smtp_pass=smtp_pass,
    )
