# utf8 = 'utf-8'
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.message import EmailMessage
from tian_core.logger import logger
from string import Template
import os

class EmailTemplateLoader:
    def __init__(self, template_dir = None):
        if template_dir is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            template_dir = os.path.join(current_dir, 'templates')
            print(template_dir)
        print(template_dir)
        self.template_dir = template_dir
        self.templates = self.load_templates()

    def load_templates(self):
        templates = {}
        for filename in os.listdir(self.template_dir):
            if filename.endswith('.html'):
                logger.info(f"Loading template: {filename}")
                with open(os.path.join(self.template_dir, filename), 'r', encoding='utf-8') as file:
                    templates[filename] = Template(file.read())
        return templates

    def get_template_names(self):
        return list(self.templates.keys())

    def get_template_content(self, template_name, data=None):
        template = self.templates.get(template_name)
        if not template:
            raise ValueError(f"Template '{template_name}' not found.")
        print(data)
        return template.safe_substitute(data or {})

    def send_email(self, template_name, data,  to_email, subject, smtp_server, smtp_port, smtp_user, smtp_pass):
        template_content = self.get_template_content(template_name, data)
        if not template_content:
            raise ValueError("Template not found!")

        msg = EmailMessage()
        msg.set_content(template_content, subtype='html')
        msg['Subject'] = subject
        msg['From'] = "open@thienhang.com"
        msg['To'] = to_email

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)

