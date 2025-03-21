import json

from google.cloud.storage import Bucket


def google_load_bucket_json(bucket: Bucket, file_to_read_full_path: str):
    """

    :param bucket:
    :param file_to_read_full_path:
    :return:
    """
    # Load bucket path
    blob = bucket.blob(file_to_read_full_path)
    try:
        with blob.open("r") as f:
            content = f.read()
        return json.loads(content)
    except Exception as e:
        print(f"google_load_bucket_json() · Could not load bucket path because {e}")

        # Write blank file
        print(f"google_load_bucket_json · Writing blank json")
        with blob.open("w") as f:
            f.write(json.dumps([]))

        return []
