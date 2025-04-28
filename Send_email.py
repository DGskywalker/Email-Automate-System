import time
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

contacts = pd.read_csv('/Users/divyanshgupta/Desktop/ColdEmails.py/Cafes.csv') 
print(contacts.columns)

sender_email = "Your-Email"
sender_password = "Your-Email-App-Pass"  

subject = "Bot Mails Testing"

for index, row in contacts.iterrows():
    receiver_email = row['Email']
    restaurant_name = row['Name']

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    body = f"""
    Hi {restaurant_name},

     Hi, This is an automated bot generated message. Dont react to it !!!

    """

    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"✅ Email sent to {receiver_email}")
    except Exception as e:
        print(f"❌ Failed to send to {receiver_email}: {e}")
    time.sleep(10)