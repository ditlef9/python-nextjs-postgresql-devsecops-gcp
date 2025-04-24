import json
import os

import flask
import functions_framework

from src.email.send_email import send_email
from src.limacharlie.auth_limacharlie import auth_limacharlie
from src.limacharlie.sensors_list import sensors_list
from src.spreadsheet.spreadsheet import spreadsheet
from src.utils.get_datetime import get_datetime
from src.utils.google_bucket_storage_client_and_get_bucket import google_bucket_storage_client_and_get_bucket
from src.utils.google_bucket_write_from_filename import google_bucket_write_from_filename
from src.utils.google_secret_manager_access_secret_version import google_secret_manager_access_secret_version


@functions_framework.http
def main(request: flask.wrappers.Request):
    log_headline: str = f"main()"
    print(f"{log_headline} · Init")

    # DT
    dt_info = get_datetime()


    # Read secret
    try:
        google_cloud_project_id = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
        secret_str = google_secret_manager_access_secret_version(project_id=google_cloud_project_id, secret_id="report-excel-services")
    except Exception as e:
        print(f"{log_headline}· Could not access google secret e={e}")
        raise Exception(f"{log_headline}· Could not access google secret e={e}")
    secret_dict: dict = json.loads(secret_str)
    gmail_sender_email: str = secret_dict['gmail_sender_email']
    gmail_app_password: str = secret_dict['gmail_app_password']
    recipient_email_addresses: str = secret_dict['recipient_email_addresses']
    limacharlie_organization_id: str = secret_dict['limacharlie_organization_id']
    limacharlie_api_key: str = secret_dict['limacharlie_api_key']

    # Authenticate
    limacharlie_token = auth_limacharlie(limacharlie_organization_id=limacharlie_organization_id, limacharlie_api_key=limacharlie_api_key)

    # List sensors
    limacharlie_sensors_list = sensors_list(limacharlie_organization_id=limacharlie_organization_id, limacharlie_token=limacharlie_token)

    # Generate XLSX Spreadsheet
    spreadsheet(datetime_ym=dt_info['ym'], limacharlie_sensors_list=limacharlie_sensors_list)

    # Upload to bucket
    storage_client, bucket = google_bucket_storage_client_and_get_bucket(bucket_name="report-excel-bucket")
    google_bucket_write_from_filename(bucket=bucket,
                                      file_to_upload_full_path=f"_tmp/sensors-{dt_info['ym']}.xlsx",
                                      bucket_target_full_path=f"sensors-{dt_info['ym']}.xlsx")

    # Send as email
    send_email(gmail_sender_email=gmail_sender_email,
               gmail_app_password=gmail_app_password,
               recipient_email_addresses=recipient_email_addresses,
               sensors_file_full_path=f"_tmp/sensors-{dt_info['ym']}.xlsx",
               datetime_by=dt_info['by'],
               limacharlie_organization_id=limacharlie_organization_id)

    return {"message": f"Ok", "data": None, "error": "Success"}, 200

# - Main start ----------------------------------------------------------------
if __name__ == "__main__":
    # Dev only: run "python main.py"
    #
    # Set Environment variable GOOGLE_CLOUD_PROJECT_ID
    # PyCharm > Edit Configuration > Python
    #
    #     Name: main
    #     Script: main.py
    #     Environment variables: PYTHONUNBUFFERED=1;GOOGLE_CLOUD_PROJECT_ID=applications-dev-453706
    #
    #
    print("main() · Flask API running in Developing Mode")
    print("main() · Login with: gcloud auth application-default login")
    app = flask.Flask(__name__)  # Create a Flask app instance
    request = flask.request
    main(request)
