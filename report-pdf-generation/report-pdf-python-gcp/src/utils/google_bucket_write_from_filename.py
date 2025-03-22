
from google.cloud.storage import Bucket


def google_bucket_write_from_filename(bucket: Bucket, file_to_upload_full_path: str, bucket_target_full_path: str):
    """

    :param bucket:
    :param bucket_path:
    :param filename_full_path:
    :return:
    """

    # Write to bucket path
    blob = bucket.blob(bucket_target_full_path)
    try:
        blob.upload_from_filename(file_to_upload_full_path)

    except Exception as e:
        print(f"google_bucket_write_blob() · Could not write to bucket path because {e}")

