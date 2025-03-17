import json

import flask
import functions_framework
from google.cloud import storage

from src.get_version_github import get_version_github
from src.get_version_list import get_version_list
from src.send_email import send_email
from src.utils.google_bucket_load_json import google_bucket_load_json
from src.utils.google_bucket_write_json import google_bucket_write_json


@functions_framework.http
def main(request: flask.wrappers.Request):
    """
    Checks the latest versions of various applications from different sources,
    compares them with stored versions in a Google Cloud Storage bucket,
    and sends an email if any updates are found.
    """
    log_headline: str = f"main()"
    print(f"{log_headline} · Init")

    # Applications list
    with open("applications_list.json", "r") as f:
        applications_list: list = json.load(f)

    # Get versions stored in bucket
    client = storage.Client()
    bucket = client.get_bucket(bucket_or_name="versions-tracker-bucket")
    stored_bucket_data_list = google_bucket_load_json(bucket=bucket, bucket_path="bucket_versions.json")


    # Input variable
    inp_data_to_bucket_list: list = []
    found_changes: bool = False

    # Find versions of all applications
    for application_dict in applications_list:
        application_name = application_dict['name']
        application_website_url = application_dict['website_url']
        application_version_url = application_dict['version_url']
        application_version_check_function = application_dict['version_check_function']

        # Headline
        print(f"{log_headline} {application_name} ---------------------------------")

        # Get latest version
        if application_version_check_function == "get_version_github.py":
            found_latest_version = get_version_github(application_version_url)
        elif application_version_check_function == "get_version_list.py":
            found_latest_version = get_version_list(application_version_url)
        else:
            raise Exception("Error: Function not implemented!")
        print(f"{log_headline} {application_name} Found latest version: {found_latest_version}")

        # Check the version stored in our bucket
        bucket_version: str = "NOT FOUND"
        for stored_bucket_data_dict in stored_bucket_data_list:
            if stored_bucket_data_dict['bucket_entry_name'] == application_name:
                bucket_version = stored_bucket_data_dict['bucket_entry_version']

        # Compare version
        if found_latest_version != bucket_version:
            print(f"{log_headline} {application_name} New version!")
            found_changes = True  # We will set new changes
            is_new_version = True
        else:
            is_new_version = False

        # Input data to Bucket
        inp_entry_dictionary: dict = {
          "bucket_entry_name": application_name,
          "bucket_entry_website_url": application_website_url,
          "bucket_entry_version_url": application_version_url,
          "bucket_entry_version_check_function": application_version_check_function,
          "bucket_entry_version": found_latest_version,
          "bucket_entry_is_new_version": is_new_version
        }
        inp_data_to_bucket_list.append(inp_entry_dictionary)

    # Found changes? Then write it to bucket and send email
    if found_changes:
        google_bucket_write_json(bucket=bucket, bucket_path="bucket_versions.json", inp_data_list=inp_data_to_bucket_list)

        # Send email
        send_email(inp_data_to_bucket_list=inp_data_to_bucket_list)


if __name__ == '__main__':
    print("versions-tracker local run")
    print(f"Remember to login with: gcloud auth application-default login")

    app = flask.Flask(__name__)  # Create a Flask app instance
    request = flask.request
    main(request)
