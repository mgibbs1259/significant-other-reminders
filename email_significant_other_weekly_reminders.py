import os
import logging
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import credentials


def email_significant_other():
    """Send an email to the significant other."""
    # Set up the email
    message = MIMEMultipart("alternative")
    message["From"] = credentials.sender_email_credentials["sender_email_address"]
    message["To"] = credentials.recipient_email_credentials["recipient_email_address"]
    message["Subject"] = "Weekly Reminders"
    with open(os.path.abspath("significant-other-reminders/weekly_reminders.txt"), "r") as weekly_reminders:
        text = weekly_reminders.read()
    message_text = MIMEText(text, "plain")
    message.attach(message_text)
    # Send the email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(message["From"], credentials.sender_email_credentials["sender_email_password"])
            server.sendmail(message["From"], message["To"], message.as_string())
    except Exception as e:
        logger.error(e, exc_info=True)


if __name__ == "__main__":
    logging.basicConfig(filename="/tmp/email_signigicant_other.log", filemode="w", level=logging.ERROR,
                        format="%(asctime)s %(levelname)s %(message)s")
    logger = logging.getLogger(__name__)
    email_significant_other()
