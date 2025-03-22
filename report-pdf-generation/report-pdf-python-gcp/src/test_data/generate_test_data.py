import random

from src.utils.get_datetime import get_datetime
from src.utils.google_bucket_storage_client_and_get_bucket import google_bucket_storage_client_and_get_bucket
from src.utils.google_bucket_write_json import google_bucket_write_json


def generate_test_data(number_of_assets: int = 10):
    """
    generates test data of the following format:

        test_asset_dict:
        {
            "asset_name": "...",
            "asset_external_ip": "...",
            "asset_internal_ip": "...",
            "asset_type": "client/server",
            "asset_risk_score": "",
            "vulnerability_list": [
                "title": "..:",
                "severity": "critical/high/medium/low",
                "description": "...",
                "how_to_fix": "...",
                "link": "...."
            ]
        }

    The test data is stored in google bucket:
        report-pdf-bucket/data/YYYY-MM/asset_name_slug.json

    :param number_of_assets: Number of test assets to generate.
    :return:
    """

    # Datetime
    dt_info = get_datetime()
    datetime_ym = dt_info['ym']

    # Load bucket
    storage_client, bucket = google_bucket_storage_client_and_get_bucket(bucket_name="report-pdf-bucket")

    # Severity levels
    severity_levels = ["critical", "high", "medium", "low"]

    # Asset categories for more realistic names
    asset_categories = {
        "server": ["web-server", "database", "vpn-gateway"],
        "client": ["finance-workstation", "engineering-laptop"]
    }

    for i in range(number_of_assets):
        asset_type = random.choice(list(asset_categories.keys()))
        asset_name = f"{random.choice(asset_categories[asset_type])}-{random.randint(1, 99):02d}"
        asset_data_dict = {
            "asset_name": asset_name,
            "asset_external_ip": f"192.168.1.{random.randint(1, 255)}",
            "asset_internal_ip": f"10.0.0.{random.randint(1, 255)}",
            "asset_type": asset_type,
            "asset_risk_score": round(random.uniform(0, 10), 2),
            "vulnerability_list": [
                {
                    "title": f"CVE-{j}",
                    "severity": random.choice(severity_levels),
                    "description": f"Description for {j}",
                    "how_to_fix": f"Fix instructions for {j}",
                    "link": f"https://vuln-db.example.com/{j}"
                } for j in range(random.randint(1, 5))
            ]
        }

        # Define file path (YYYY-MM/asset_name_slug.json)
        asset_slug = asset_name.replace(" ", "_").lower()
        file_to_write_to_full_path = f"data/{datetime_ym}/{asset_slug}.json"

        # Upload data
        google_bucket_write_json(bucket=bucket, file_to_write_to_full_path=file_to_write_to_full_path, data_to_write=asset_data_dict)

        # Print to screen
        print(f"generate_test_data() · Wrote {file_to_write_to_full_path}")

if __name__ == "__main__":
    # Howto use:
    #   PyCharm > Edit Configuration >
    #   Name: generate_test_data
    #   Script: generate_test_data.py
    #   Environment variables: PYTHONUNBUFFERED=1;GOOGLE_CLOUD_PROJECT_ID=applications-dev-453706
    #
    generate_test_data(number_of_assets=10)

