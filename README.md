# Python Email Sending Script

This script demonstrates how to send an email using Python's `smtplib` library along with `email.mime` classes to create a MIME-compliant email.

## Prerequisites

Ensure you have Python installed on your system. This script uses the built-in `smtplib` library, so no additional packages are required.

## Configuration

Before running the script, make sure to replace the placeholder values with your actual email credentials and email addresses.

```python
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email_address'
smtp_password = 'your_email_app_password'

email_from  = "your_email"
email_to = "recipient_email_address"
subject = "This is Subject"
body = "This is Body"
