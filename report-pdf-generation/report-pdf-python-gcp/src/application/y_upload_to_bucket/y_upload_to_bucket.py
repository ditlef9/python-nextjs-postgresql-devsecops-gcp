from google.cloud.storage import Bucket

from src.utils.google_bucket_write_from_filename import google_bucket_write_from_filename


def y_upload_to_bucket(bucket: Bucket, pdf_file_full_path: str, bucket_target_full_path: str):

    print("main()·y_upload_to_bucket() · Uploading PDF to ")
    google_bucket_write_from_filename(bucket=bucket,
                                      file_to_upload_full_path=pdf_file_full_path,
                                      bucket_target_full_path=bucket_target_full_path)
