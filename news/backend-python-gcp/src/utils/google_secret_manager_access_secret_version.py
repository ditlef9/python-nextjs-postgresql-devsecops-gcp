from google.cloud import secretmanager
import hashlib


def google_secret_manager_access_secret_version(project_id: str, secret_id: str, version_id: str = "latest"):
    """
    Accesses a secret from Google Secret Manager.

    :param project_id: Google Cloud project ID.
    :param secret_id: The ID of the secret to retrieve.
    :param version_id: The version of the secret to retrieve (default is "latest").
    :return: The secret value as a decoded string.

    Documentation: https://codelabs.developers.google.com/codelabs/secret-manager-python#6
    """
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Return the decoded payload.
    return response.payload.data.decode('UTF-8')

