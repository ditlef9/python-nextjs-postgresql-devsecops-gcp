import json
import os

from src.utils.google_secret_manager_access_secret_version import google_secret_manager_access_secret_version
from src.utils.send_gmail_app_pass import send_gmail_app_pass


def z_send_email(datetime_ym: str, datetime_by: str):
    """
    Sends an email

    :param
    """
    log_headline: str = f"main()·z_send_email()"
    print(f"{log_headline} · Init")

    # Read secret
    try:
        google_cloud_project_id = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
        secret_str = google_secret_manager_access_secret_version(project_id=google_cloud_project_id, secret_id="report-pdf-services")
    except Exception as e:
        print(f"{log_headline} Could not access google secret e={e}")
        raise Exception(f"main()·send_email() Could not access google secret e={e}")
    secret_dict: dict = json.loads(secret_str)
    gmail_sender_email: str = secret_dict['gmail_sender_email']
    gmail_app_password: str = secret_dict['gmail_app_password']
    recipient_email_addresses: str = secret_dict['recipient_email_addresses']

    # Subject
    subject = f"Monthly Report - Asset Security Report for {datetime_by}"

    # Body
    body = (
        f"Dear Team,\n\n"
        f"Please find attached the Asset Security Report for {datetime_by}. This report provides a detailed analysis of vulnerabilities detected within the monitored assets.\n\n"
        f"🔍 Key Highlights:\n"
        f"- Comprehensive vulnerability assessment\n"
        f"- Categorization based on severity levels\n"
        f"- Recommended actions for mitigation\n\n"
        f"For any questions or further clarifications, feel free to reach out.\n\n"
        f"Best regards,\n"
        f"Your Security Team\n\n"
        f"📌 To unsubscribe from these reports, reply with 'Unsubscribe' in the subject line."
    )

    # Attachment
    attachment_path = f"_tmp/report-{datetime_ym}.pdf"

    # Send!
    send_gmail_app_pass(gmail_sender_email=gmail_sender_email, gmail_app_password=gmail_app_password, recipient_email_addresses=recipient_email_addresses, subject=subject, body=body, attachment_path=attachment_path)


