# src/limacharlie/auth_limacharlie.py
import requests


def auth_limacharlie(limacharlie_organization_id: str, limacharlie_api_key: str):
    """

    :return:
    """
    url = f"https://app.limacharlie.io/jwt/"
    headers = {"Content-Type": "application/json"}
    body = {
        "oid": limacharlie_organization_id,
        "secret": limacharlie_api_key,
    }

    try:
        response = requests.post(url=url, json=body, headers=headers)
    except Exception as e:
        print(f"auth_limacharlie() · Error getting LC token: {e}")  # noqa

        return ""

    if response.status_code == 200:
        # Print response
        try:
            jwt_token = response.json()
            return jwt_token['jwt']
        except Exception as e:
            print(f"auth_limacharlie() · Error Response JSON: {response} ({e})")
            return ""
    else:
        print(f"auth_limacharlie() · Error response was not 200 when getting LC token: {response.status_code}")  # noqa
        return ""
