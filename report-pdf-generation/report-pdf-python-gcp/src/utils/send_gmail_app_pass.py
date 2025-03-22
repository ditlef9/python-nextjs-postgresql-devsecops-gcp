import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_gmail_app_pass(
        gmail_sender_email: str,
        gmail_app_password: str,
        recipient_email_addresses: str,
        subject: str,
        body: str,
        attachment_path: str = None):
    """
    Send an email using Gmail with an optional attachment.

    :param gmail_sender_email: Gmail address of the sender
    :param gmail_app_password: Generated app password from Google
    :param recipient_email_addresses: Email address of the recipient
    :param subject: Email subject
    :param body: Email body content
    :param attachment_path: File path of the attachment (default: None)
    :return: None
    """
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg["From"] = gmail_sender_email
        msg["To"] = recipient_email_addresses
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Attach file if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment_file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment_file.read())

            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(attachment_path)}"
            )
            msg.attach(part)
            print(f"Attached file: {attachment_path}")

        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(gmail_sender_email, gmail_app_password)  # Login using app password

        # Send the email
        server.sendmail(gmail_sender_email, recipient_email_addresses, msg.as_string())

        # Close the connection
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")


# Example usage:
if __name__ == "__main__":
    send_gmail_app_pass(
        gmail_sender_email="your_email@gmail.com",
        gmail_app_password="your_app_password",  # Replace with your app password
        recipient_email_addresses="recipient@example.com",
        subject="Test Email with Attachment",
        body="Hello, this is a test email sent via Python with an attachment!",
        attachment_path="_tmp/severity_chart.png"  # Replace with the actual file path
    )
