from flask_mail import *
from dotenv import load_dotenv
import os

class Email:
    # **************************MAIL CONFIGURATION**************
    def __init__(self,app):
        app.config["MAIL_SERVER"]="smtp.office365.com"
        app.config["MAIL_PORT"]="587"
        app.config["MAIL_USERNAME"]=os.getenv("user_name")
        app.config["MAIL_PASSWORD"]=os.getenv("passoword")
        app.config["MAIL_USE_TLS"]=True
        app.config["MAIL_USE_SSL"]=False
        self.mail=Mail(app)  #mail object

    def compose_mail(self,subject,email,message):
        msg=Message(subject,
                    sender="rishabhraaj10006@outlook.com",
                    recipients=[email])
        msg.body=message
        self.mail.send(msg)
        