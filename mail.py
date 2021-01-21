import smtplib
from credentials import *
from email.message import EmailMessage


def shoot_mail(subject, body):
    msg = EmailMessage()
    msg['Subject'] = f'Homerun Automation - {subject}'
    msg['From'] = emailAddress
    msg['To'] = send_mail_to
    msg.set_content(f'{body}')

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(emailAddress, emailPassword)
    s.send_message(msg)
    # terminating the session
    s.quit()
    print("Success")

