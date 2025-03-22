import os
from google.cloud import storage


def google_bucket_storage_client_and_get_bucket(bucket_name: str):
    """
    Creates a Google Cloud Storage client and returns the bucket.

    :param bucket_name: The name of the bucket to retrieve
    :return: The bucket object
    """
    # Get the project ID from environment variables
    google_cloud_project_id = os.getenv('GOOGLE_CLOUD_PROJECT_ID')

    if not google_cloud_project_id:
        raise ValueError("google_bucket_storage_client_and_get_bucket() · GOOGLE_CLOUD_PROJECT_ID environment variable is not set.")

    # Create the Google Cloud Storage client with the project ID from the environment variable
    storage_client = storage.Client(project=google_cloud_project_id)

    # Get the bucket from the client
    bucket = storage_client.get_bucket(bucket_name)

    return storage_client, bucket
