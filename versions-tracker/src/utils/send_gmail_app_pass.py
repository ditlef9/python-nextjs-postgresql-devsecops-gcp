import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_gmail_app_pass(
        gmail_sender_email: str,
        gmail_app_password: str,
        recipient_email_addresses: str,
        subject: str,
        body: str):
    """
    Send an email using Gmail with an app password.

    How to get an app password:
    1) Enable Two-Factor Authentication (2FA)
    2) Go to the App Passwords page on Google: https://myaccount.google.com/apppasswords
    3) Generate a password for "Mail" and copy it

    * If you get an authentication error, check if "Less Secure Apps" is disabled in Google Security.
    * Google may block the sign-in attempt if it detects an untrusted location.

    :param sender_email: Gmail address of the sender
    :param app_password: Generated app password from Google
    :param recipient_email: Email address of the recipient
    :param subject: Email subject
    :param body: Email body content
    :return: None
    """
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg["From"] = gmail_sender_email
        msg["To"] = recipient_email_addresses
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

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


# Example usage
if __name__ == "__main__":
    send_gmail_app_pass(
        sender_email="your_email@gmail.com",
        app_password="your_app_password",  # Replace with your app password
        recipient_email="recipient@example.com",
        subject="Test Email",
        body="Hello, this is a test email sent via Python!"
    )
