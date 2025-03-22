from src.utils.send_gmail_app_pass import send_gmail_app_pass


def send_email(gmail_sender_email: str,
               gmail_app_password: str,
               recipient_email_addresses: str,
               sensors_file_full_path: str,
               datetime_by: str,
               limacharlie_organization_id: str):
    """
    Sends an email

    :param
    """
    log_headline: str = f"main()·send_email()"
    print(f"{log_headline} · Init")

    # Subject
    subject = f"Monthly Report - LimaCharlie Sensors List for {datetime_by} for {limacharlie_organization_id}"

    # Body
    body = (
        f"Dear Team,\n\n"
        f"Please find attached the Sensors List for {datetime_by}.\n\n"
        f"LimaCharlie org: {limacharlie_organization_id}\n"
        f"LimaCharlie URL: https://app.limacharlie.io/orgs/{limacharlie_organization_id}/sensors\n\n"
        f"For any questions or further clarifications, feel free to reach out.\n\n"
        f"Best regards,\n"
        f"Your Security Team\n\n"
        f"📌 To unsubscribe from these reports, reply with 'Unsubscribe' in the subject line."
    )


    # Send!
    send_gmail_app_pass(gmail_sender_email=gmail_sender_email, gmail_app_password=gmail_app_password, recipient_email_addresses=recipient_email_addresses, subject=subject, body=body, attachment_path=sensors_file_full_path)


