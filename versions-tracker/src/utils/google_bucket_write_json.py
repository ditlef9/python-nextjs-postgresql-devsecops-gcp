import json

import google
from google.cloud import storage


def google_bucket_write_json(bucket: google.cloud.storage.bucket.Bucket, bucket_path: str, inp_data_list: list):
    """
    Writes a list of data as a JSON file to a Google Cloud Storage bucket.

    :param bucket: Google Cloud Storage Bucket object.
    :param bucket_path: Path to the JSON file in the bucket.
    :param inp_data_list: List of data to be written as JSON.
    :return: None
    """

    # Write to bucket path
    blob = bucket.blob(bucket_path)
    try:
        with blob.open("w") as f:
            f.write(json.dumps(inp_data_list))
    except Exception as e:
        print(f"google_bucket_write_json()·Could not write to bucket path because {e}")

