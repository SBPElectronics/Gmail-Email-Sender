#Getting a Gmail App Password:

#Go to your Google Account → Security
#Enable 2-Step Verification if not already on
#Search for "App Passwords" → create one for "Mail"
#Paste the 16-character password into APP_PASSWORD

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Config
EMAIL = "you@gmail.com"
APP_PASSWORD = "xxxx xxxx xxxx xxxx"  # Gmail App Password (not your real password)

# Build email
msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = EMAIL
msg["Subject"] = "Test Email from Python"
msg.attach(MIMEText("Hello from Python!", "plain"))

# Send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.sendmail(EMAIL, EMAIL, msg.as_string())

print("Email sent!")

