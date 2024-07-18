import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email_address'
smtp_password = 'your_email_app_password'

email_from  = "youtr_email"
email_to = "recipitent_email_address"
subject = "This is Subject"
body = "This is Body"

message = MIMEMultipart()
message["From"] =  email_from
message["To"] =  email_to
message["Subject"] =  subject

message.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(email_from, email_to, message.as_string())
    print(f"Email sent to {email_to} successfully.")
except Exception as e:
    print(f"Emil sent to {email_to} failed becuase {e}")
finally:
    server.quit()
