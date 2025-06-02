from tian_core import AbstractNotification
from tian_core.logger import logger

from tian_utils.email import EmailTemplateLoader

class EmailNotification(AbstractNotification):
    def __init__(self):
        self.loader = EmailTemplateLoader()
        logger.info("[ INIT ] > EmailNotification initialized")

    def send(self):
        # msg = f"Subject: allocation service notification\n{message}"
        # self.server.sendmail(
        #     from_addr="open@thienhang.com",
        #     to_addrs=[destination],
        #     msg=msg,
        # )
        self.loader.send_email(
                    template_name='comment-notification.html',
                    to_email="hangtuanthiendl@gmail.com",
                    subject='Bạn vừa đăng nhập vào hệ thống develope@thienhang',
                    smtp_server='smtp.sendgrid.net',
                    smtp_port=465,
                    smtp_user='apikey',
                    smtp_pass='',
                    data={
                        'username': 'thienhang',
                        'email': 'me@thienhang.com',
                        'password': 'password',
                        'link': 'https://dev.thienhang.com',
                    }
                )
        print("Sending email...")



def send_account_successfully_email(email): #TODO: 
    import os
    dir = os.getcwd() + "/templates/email"
    loader = EmailTemplateLoader(
        template_dir=dir
    )
    loader.send_email(
        template_name="org-invitation.html",
        to_email=email,
        subject="🚀 Account Notification | developer@thienhang",
        smtp_server="smtp.sendgrid.net",
        smtp_port=465,
        smtp_user="apikey",
        smtp_pass="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",
        data=email
    )


def send_active_user_email(data): #TODO: 
    import os
    dir = os.getcwd() + "/templates/email"
    loader = EmailTemplateLoader(
        template_dir=dir
    )
    loader.send_email(
        template_name="verify-email",
        to_email=data["email"],
        subject="🚀 Account Notification | developer@thienhang",
        smtp_server="smtp.sendgrid.net",
        smtp_port=465,
        smtp_user="apikey",
        smtp_pass="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",
        data=data
    )


def renew_password(data): #TODO: 
    import os
    dir = os.getcwd() + "/templates/email"
    loader = EmailTemplateLoader(
        template_dir=dir
    )
    loader.send_email(
        template_name="resetpassword.html",
        to_email=data["email"],
        subject="🚀 Account Notification | developer@thienhang",
        smtp_server="smtp.sendgrid.net",
        smtp_port=465,
        smtp_user="apikey",
        smtp_pass="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",
        data=data
    )