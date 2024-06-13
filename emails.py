#!/usr/bin/env python3

# Import the required modules
import email.message
import mimetypes
import os
import smtplib

# Function to generate the email message
def generate_email(sender, receiver, subject, body, attachment=None):
    """Generates an email message with an attachment."""
    # Email basic structure
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    # Process the message attachment if exists
    if attachment:
        filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_main, mime_sub = mime_type.split("/", 1)

        with open(attachment, "rb") as attachment_file:
            message.add_attachment(
                attachment_file.read(),
                maintype=mime_main,
                subtype=mime_sub,
                filename=filename,
            )
            
    return message

# Function to send the email message
def send_email(message):
    """ Sends the email message to a SMTP server."""
    with smtplib.SMTP("localhost") as mail_server:
        mail_server.send_message(message)
