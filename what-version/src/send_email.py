import json

from src.utils.google_secret_manager_access_secret_version import google_secret_manager_access_secret_version
from src.utils.send_gmail_app_pass import send_gmail_app_pass


def send_email(inp_data_to_bucket_list: list):
    """
    Sends an email notification if new software versions are available.

    :param inp_data_to_bucket_list: [{'bucket_entry_name': 'Python', 'bucket_entry_website_url': 'https://www.python.org', 'bucket_entry_version_url': 'https://www.python.org/ftp/python', 'bucket_entry_version_check_function': 'get_version_list.py', 'bucket_entry_version': '3.14.0', 'bucket_entry_is_new_version': False}, {'bucket_entry_name': 'Node.js', 'bucket_entry_website_url': 'https://nodejs.org/en', 'bucket_entry_version_url': 'https://nodejs.org/download/release', 'bucket_entry_version_check_function': 'get_version_list.py', 'bucket_entry_version': 'v23.10.0', 'bucket_entry_is_new_version': True}, {'bucket_entry_name': 'Git', 'bucket_entry_website_url': 'https://git-scm.com', 'bucket_entry_version_url': 'https://github.com/git-for-windows/git/releases', 'bucket_entry_version_check_function': 'get_version_github.py', 'bucket_entry_version': '8.12.1', 'bucket_entry_is_new_version': True}]
    :return:
    """
    log_headline: str = f"main()·send_email()"
    print(f"{log_headline} · Init")

    # Read secret
    try:
        secret_str = google_secret_manager_access_secret_version(project_id="applications-dev-453706", secret_id="what-version-services")
    except Exception as e:
        print(f"{log_headline} Could not access google secret e={e}")
        raise Exception(f"main()·send_email() Could not access google secret e={e}")
    secret_list: list = json.loads(secret_str)
    gmail_sender_email: str = secret_list['gmail_sender_email']
    gmail_app_password: str = secret_list['gmail_app_password']
    recipient_email_addresses: str = secret_list['recipient_email_addresses']

    # Filter new versions
    new_versions = [entry for entry in inp_data_to_bucket_list if entry["bucket_entry_is_new_version"]]
    all_software = [entry["bucket_entry_name"] for entry in inp_data_to_bucket_list]

    # Subject addresses
    new_version_names = ", ".join(entry["bucket_entry_name"] for entry in new_versions)
    subject = f"New Versions Available: {new_version_names}"

    # Body

    body = "🔔 Software Version Update Notification 🔔\n\n"
    body += "Here are the latest software versions:\n\n"

    for entry in inp_data_to_bucket_list:
        name = entry["bucket_entry_name"]
        website = entry["bucket_entry_website_url"]
        version_url = entry["bucket_entry_version_url"]
        version = entry["bucket_entry_version"]
        is_new = "🆕 New Version Available!" if entry["bucket_entry_is_new_version"] else "✅ Up-to-date"

        body += f"{name}\n"
        body += f"- Version: {version}\n"
        body += f"- Status: {is_new}\n"
        body += f"- Website: {website}\n"
        body += f"- Download: {version_url}\n\n"

    body += "\nBest regards,\n"
    body += "Your Automated Version Tracker 🤖\n"
    body += "To unsubscribe reply to this email with 'Unsubscribe' in subject.\n"

    # Send!
    send_gmail_app_pass(gmail_sender_email=gmail_sender_email, gmail_app_password=gmail_app_password, recipient_email_addresses=recipient_email_addresses, subject=subject, body=body)


# Example Usage
if __name__ == "__main__":
    example_data = [
        {
            "bucket_entry_name": "Python",
            "bucket_entry_website_url": "https://www.python.org",
            "bucket_entry_version_url": "https://www.python.org/ftp/python",
            "bucket_entry_version_check_function": "get_version_list.py",
            "bucket_entry_version": "3.14.0",
            "bucket_entry_is_new_version": False,
        },
        {
            "bucket_entry_name": "Node.js",
            "bucket_entry_website_url": "https://nodejs.org/en",
            "bucket_entry_version_url": "https://nodejs.org/download/release",
            "bucket_entry_version_check_function": "get_version_list.py",
            "bucket_entry_version": "v23.10.0",
            "bucket_entry_is_new_version": True,
        }
    ]

    send_email(example_data)