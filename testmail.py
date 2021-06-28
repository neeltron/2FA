import smtplib
from email.mime.multipart import MIMEMultipart
import os

sender_address = os.environ['email']
sender_pass = os.environ['pass']
receiver_address = 'nprosofficial@gmail.com'

message = MIMEMultipart()

message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
