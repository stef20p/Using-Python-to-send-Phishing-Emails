import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

email = EmailMessage()

email['from'] = 'Stefan Paunovic'
email['to'] = 'stef20p@gmail.com'
email['subject'] = 'you won a million dollars'

email.set_content('USE THIS {link} TO CLAIM YOUR REWARD!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('stef20p@gmail.com', 'bqdktwessnyuowmh')
    smtp.send_message(email)
    print('all good boss!')
