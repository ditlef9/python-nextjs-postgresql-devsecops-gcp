import json


def google_bucket_write_json(bucket, file_to_write_to_full_path, data_to_write):
    # Write to bucket path
    blob = bucket.blob(file_to_write_to_full_path)
    try:
        with blob.open("w") as f:
            f.write(json.dumps(data_to_write, indent=4))
    except Exception as e:
        print(f"google_write_bucket_json() ·  Could not write to bucket path because {e}")

