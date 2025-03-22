# src/spreadsheet/spreadsheet.py
import os
import pandas as pd

def spreadsheet(datetime_ym: str, limacharlie_sensors_list: list):
    """

    The spreadsheet is stored to _tmp/report-ym.xlsx

    Spreadsheet rows:
    * Hostname
    * Enroll
    * SID


    Sensors list:
    [{'alive': '2025-03-22 06:41:00', 'arch': 9, 'did': '', 'enroll': '2025-03-22 06:22:44', 'ext_ip': 'internal', 'ext_plat': 0, 'hostname': 'Finance application', 'int_ip': '', 'is_isolated': False, 'is_kernel_available': False, 'is_online': True, 'mac_addr': '', 'oid': 'a65162e8-2493-4d2f-a136-03f680dd2180', 'plat': 2415919104, 'sealed': False, 'should_isolate': False, 'should_seal': False, 'sid': '1948b1c0-bb85-481e-97f8-86a11348ea33'}]


    :param datetime_ym: Year and month in format 'YYYY-MM'
    :param limacharlie_sensors_list: List of sensor dictionaries
    :return:
    """
    # Generate excel
    # Ensure output directory exists
    output_dir = "_tmp"
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    file_path = os.path.join(output_dir, f"sensors-{datetime_ym}.xlsx")

    # Extract relevant data from sensors list
    data = [{
        "Hostname": sensor.get("hostname", "Unknown"),
        "Enroll": sensor.get("enroll", "Unknown"),
        "SID": sensor.get("sid", "Unknown")
    } for sensor in limacharlie_sensors_list]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to Excel
    df.to_excel(file_path, index=False)

    print(f"spreadsheet() · Spreadsheet saved to {file_path}")
