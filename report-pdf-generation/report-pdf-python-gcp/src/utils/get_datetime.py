# Version 2
from datetime import datetime

def get_datetime():
    """
    Returns the current datetime in multiple formats.

    Usage:
      dt_info = get_datetime()

      One day forward??
      One month forward??
      First day of month??

      print("Date time:", dt_info["ymdhms"]) # 2025-03-18 12:34:56
      print("Timestamp:", dt_info["timestamp"]) # 1710765296.789012

    :return: Dictionary with different datetime formats.
    """
    now = datetime.now()

    # Get time zone
    timezone_offset: str = now.strftime("%z")  # +0200
    formatted_timezone: str = f"UTC{timezone_offset[:3]}"  # timezone_offset[:3] gives the "+02" part
    if formatted_timezone == "UTC+00":
        formatted_timezone = "UTC"


    datetime_ymdhms: str = now.strftime("%Y-%m-%d %H:%M:%S")
    datetime_ymdhms_saying: str = now.strftime("%d.%m.%Y %H:%M:%S") + f" {formatted_timezone}"
    datetime_ymdhms_slug: str = now.strftime("%d.%m.%Y-%H.%M.%S")
    datetime_ymd: str = now.strftime("%Y-%m-%d")
    datetime_hms: str = now.strftime("%H:%M:%S")
    datetime_ym: str = now.strftime("%Y-%m")
    datetime_by: str = now.strftime("%b %Y") # Mar 2025
    timestamp = now.timestamp()

    return {
        "now": now,  # Return the raw datetime object
        "ymdhms": datetime_ymdhms,  # Example: "2025-03-18 12:34:56"
        "ymdhms_saying": datetime_ymdhms_saying,  # Example: "2025-03-18 12:34:56"
        "ymdhms_slug": datetime_ymdhms_slug,  # Example: "21.03.2025-13.22.00"
        "ymd": datetime_ymd,  # Example: "2025-03-18 12:34:56"
        "hms": datetime_hms,  # Example: "2025-03-18 12:34:56"
        "ym": datetime_ym,  # Example: "2025-03"
        "by": datetime_by,  # Example: "Mar 2025"
        "timestamp": timestamp  # Example: 1710765296.789012
    }
