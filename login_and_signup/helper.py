from django.core.mail import send_mail
import smtplib,ssl
from email.message import EmailMessage

from django.conf import settings





def send_reset_link(email):
    
    
    subject = 'Your forget password link'
    message = f'Click on the link to reset your password http://127.0.0.1:8000/password-reset/{email}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)
    return True
    
    
    
    
    
    
    
    
    
    # msg = EmailMessage()
    # msg.set_content(f"Click on the link to reset your password http://127.0.0.1:8000/password-reset/{email}/")
    # msg["Subject"] = 'Your forget password link'
    # msg["From"] = settings.EMAIL_HOST_USER
    # msg["To"] = email
    
    # context = ssl.create_default_context()
    
    # with smtplib.SMTP("smtp.gmail.com",port=465) as smtp:
    #     smtp.starttls(context=context)
    #     smtp.login(msg["From"],"iiessmiflmhghsfz")
    #     smtp.sendmail(msg["From"],msg["To"],msg.as_string)