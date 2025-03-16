import requests
from bs4 import BeautifulSoup
import re


def get_version_github(url: str):
    """
    Fetches the latest version of a software from the given URL.

    :param url: The URL from which to fetch the version
    :return: The latest version (in string format)
    """
    log_headline: str = "get_version_needle()"
    print(f"{log_headline} - Fetching data from {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        version_tags = soup.find_all('a', href=True)

        version_pattern = re.compile(r'v?(\d+\.\d+\.\d+)')
        versions = [match.group(1) for tag in version_tags if (match := version_pattern.search(tag.text))]

        if not versions:
            print(f"No valid versions found at {url}")
            return None

        versions.sort(key=lambda v: list(map(int, v.split('.'))), reverse=True)
        return versions[0]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        return None

if __name__ == '__main__':
    print("get_latest_version local run")
    git_url = "https://github.com/git-for-windows/git/releases"
    latest_git_version = get_version_github(git_url)

    if latest_git_version:
        print(f"Git latest version: {latest_git_version}")
    else:
        print("Failed to fetch the latest Git version.")
