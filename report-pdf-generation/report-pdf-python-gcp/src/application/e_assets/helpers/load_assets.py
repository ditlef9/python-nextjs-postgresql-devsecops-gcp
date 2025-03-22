from google.cloud.client import Client
from google.cloud.storage import Bucket

from src.utils.google_bucket_load_json import google_load_bucket_json


def load_assets(datetime_ym: str,
                storage_client: Client,
                bucket: Bucket):
    """

    :param datetime_ym:
    :param storage_client:
    :param bucket:
    :return:
    """

    # Return value
    return_assets_list: list = []

    # Loop through all json files in bucket report-pdf-bucket/data/YYYY-MM/
    prefix = f"data/{datetime_ym}/"
    delimiter = "/"
    blobs = storage_client.list_blobs("report-pdf-bucket", prefix=prefix, delimiter=delimiter)

    # Note: The call returns a response only when the iterator is consumed.
    for blob in blobs:
        blob_name = blob.name

        # Read json
        read_asset_dict: dict = google_load_bucket_json(bucket=bucket, file_to_read_full_path=blob_name)

        # Append to our list
        return_assets_list.append(read_asset_dict)



    # Return asset list
    return return_assets_list
