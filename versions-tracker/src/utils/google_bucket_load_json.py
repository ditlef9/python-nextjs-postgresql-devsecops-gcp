import json

import google
from google.cloud import storage

def google_bucket_load_json(bucket: google.cloud.storage.bucket.Bucket, bucket_path: str):
    """
    Loads a JSON file from a Google Cloud Storage bucket.

    If the file does not exist or cannot be read, it creates an empty JSON file in the bucket and returns an empty dictionary.

    :param bucket: Google Cloud Storage Bucket object.
    :param bucket_path: Path to the JSON file in the bucket.
    :return: Parsed JSON content as a dictionary.
    """

    # Load bucket path
    blob = bucket.blob(bucket_path)
    try:
        with blob.open("r") as f:
            content = f.read()
        return json.loads(content)
    except Exception as e:
        # Write blank file
        print(f"google_bucket_load_json()·Bucker file cound not be loaded, so the script will try to write a empty bucket file. Error={e}") # noqa
        with blob.open("w") as f:
            f.write(json.dumps({}))  # Write an empty dictionary instead of []

        return {}
