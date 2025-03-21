
import flask
import functions_framework

from src.application.a_delete_old.a_delete_old import a_delete_old
from src.application.b_create_tmp.b_create_tmp import b_create_tmp
from src.application.c_generate_pdf.c_generate_pdf import c_generate_pdf
from src.application.d_graph_severity.d_graph_severity import d_graph_severity
from src.application.e_assets.e_assets import e_assets
from src.application.e_assets.helpers.load_assets import load_assets
from src.application.x_save_pdf.x_save_pdf import x_save_pdf
from src.application.y_upload_to_bucket.y_upload_to_bucket import y_upload_to_bucket
from src.application.z_send_email.z_send_email import z_send_email
from src.utils.get_datetime import get_datetime
from src.utils.google_bucket_storage_client_and_get_bucket import google_bucket_storage_client_and_get_bucket


@functions_framework.http
def main(request: flask.wrappers.Request):
    log_headline: str = f"main()"
    print(f"{log_headline} · Init")

    # DT
    dt_info = get_datetime()

    # Load bucket
    storage_client, bucket = google_bucket_storage_client_and_get_bucket(bucket_name="report-pdf-bucket")

    # A Delete old files
    a_delete_old()

    # B Create tmp dir
    b_create_tmp()

    # C generate PDF
    c = c_generate_pdf(pdf_file_full_path=f"_tmp/report-{dt_info['ym']}.pdf", datetime_ymdhms_saying=dt_info['ymdhms_saying'])

    # Fetch list of assets from GCS
    assets_list = load_assets(datetime_ym=dt_info['ym'], storage_client=storage_client, bucket=bucket)

    # D Graph
    c = d_graph_severity(c=c, assets_list=assets_list)

    # E Assets
    c = e_assets(c=c, datetime_ym=dt_info['ym'], assets_list=assets_list)

    # X Save PDF
    x_save_pdf(c)


    # Y Upload to Buckets
    y_upload_to_bucket(bucket=bucket, pdf_file_full_path=f"_tmp/report-{dt_info['ym']}.pdf", bucket_target_full_path=f"report-{dt_info['ymdhms_slug']}.pdf")

    # Send as email
    z_send_email(datetime_ym=dt_info['ym'], datetime_by=dt_info['by'])

    return {"message": f"Ok", "data": None, "error": "Success"}, 200

# - Main start ----------------------------------------------------------------
if __name__ == "__main__":
    # Dev only: run "python main.py" and open http://localhost:8080
    # Start app
    print("main()·Flask API running in Developing Mode")
    print("main()·Login with: gcloud auth application-default login")
    app = flask.Flask(__name__)  # Create a Flask app instance
    request = flask.request
    main(request)