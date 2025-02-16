import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

email = EmailMessage()

email['from'] = 'Stef XXXXX'
email['to'] = 'stxxxxXx@gmail.com'
email['subject'] = 'you won a million dollars'

email.set_content('USE THIS {link} TO CLAIM YOUR REWARD!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('stefXXXX@gmail.com', 'password')
    smtp.send_message(email)
    print('all good boss!')
