import requests
from bs4 import BeautifulSoup
import re


def get_version_list(version_url: str):
    """
    Fetches the latest version available for download from the given URL.

    :param version_url: The base URL from which to fetch the versions
    :return: The latest version (in string format)
    """
    log_headline: str = "get_version_list()"

    try:
        response = requests.get(version_url)
        response.raise_for_status()  # Raise an error if the response code is not 200 (OK)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links that might contain version numbers (directories like '3.x.x/')
        links = soup.find_all('a', href=True)

        # Regex to match semantic versioning (e.g., '3.10.2/' or 'v16.13.0/')
        version_pattern = re.compile(r'^(v?\d+\.\d+\.\d+)/$')

        versions = [link['href'].strip('/') for link in links if version_pattern.match(link['href'])]

        if not versions:
            print(f"No valid versions found at {version_url}")
            return None

        # Sort versions in descending order
        versions.sort(key=lambda v: list(map(int, re.findall(r'\d+', v))), reverse=True)
        latest_version = versions[0]

        return latest_version

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        return None


if __name__ == '__main__':
    print("get_version_list local run")
    applications_list = [
        {"name": "Python", "website_url": "https://www.python.org", "version_url": "https://www.python.org/ftp/python/"},
        {"name": "Node.js", "website_url": "https://nodejs.org/en", "version_url": "https://nodejs.org/download/release/"}
    ]

    for app in applications_list:
        name = app['name']
        website_url = app['website_url']
        version_url = app['version_url']

        # Check latest version
        print(f"{name} Checking latest version")
        latest_version = get_version_list(version_url)

        if latest_version:
            print(f"{name} latest version: {latest_version} - Confirm at {website_url}")
            print(f"{name} Checking latest version [OK]")
        else:
            print(f"{name} Failed to fetch the latest version.")
            print(f"{name} Checking latest version [Error]")
