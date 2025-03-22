import requests


def sensors_list(limacharlie_organization_id: str, limacharlie_token: str):
    """

    Example return:
    [{'alive': '2025-03-22 06:41:00', 'arch': 9, 'did': '', 'enroll': '2025-03-22 06:22:44', 'ext_ip': 'internal', 'ext_plat': 0, 'hostname': 'Finance application', 'int_ip': '', 'is_isolated': False, 'is_kernel_available': False, 'is_online': True, 'mac_addr': '', 'oid': 'a65162e8-2493-4d2f-a136-03f680dd2180', 'plat': 2415919104, 'sealed': False, 'should_isolate': False, 'should_seal': False, 'sid': '1948b1c0-bb85-481e-97f8-86a11348ea33'}]

    :return:
    """
    url = f"https://api.limacharlie.io/v1/sensors/{limacharlie_organization_id}"
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {limacharlie_token}"}

    try:
        response = requests.get(url=url, headers=headers)
    except Exception as e:
        print(f"sensors_list() · Error listing sensors: {e}")  # noqa

        return []

    if response.status_code == 200:
        # Print response
        try:
            json = response.json()
            return json['sensors']
        except Exception as e:
            print(f"sensors_list() · Error Response JSON: {response} ({e})")
            return []
    else:
        print(f"sensors_list() · Error response was not 200 when getting LC sensors: {response.status_code} {response.text}")  # noqa
        return []
