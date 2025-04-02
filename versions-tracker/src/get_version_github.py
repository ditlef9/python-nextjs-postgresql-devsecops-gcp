import requests
from bs4 import BeautifulSoup
import re

def get_version_from_filename(version_url: str):
    """
    Fetch the latest version from a filename pattern like 'Git-2.48.1-64-bit.exe'.
    """
    log_headline: str = "get_version_from_filename()"
    print(f"{log_headline} · {version_url}")

    try:
        response = requests.get(version_url)
        response.raise_for_status()

        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links containing potential versioned filenames
        links = soup.find_all('a', href=True)

        # Regex to match filenames like '*-2.48.1-64-*.exe'
        version_pattern = re.compile(r'.*-(\d+\.\d+\.\d+)-64-.*\.exe')

        versions = [match.group(1) for link in links if (match := version_pattern.search(link.text))]

        if not versions:
            print(f"{log_headline} · No valid version found for {version_url}")
            return None

        # Sort versions in descending order
        versions.sort(key=lambda v: list(map(int, v.split('.'))), reverse=True)
        latest_version = versions[0]

        return latest_version

    except requests.exceptions.RequestException as e:
        print(f"{log_headline} · Error fetching data from {version_url}: {e}")
        return None


if __name__ == '__main__':
    print("get_version_from_filename() · Running locally")

    applications_list = [
        {
            "name": "Git",
            "website_url": "https://git-scm.com",
            "version_url": "https://github.com/git-for-windows/git/releases",
            "version_check_function": "get_version_from_filename"
        }
    ]

    for application_dict in applications_list:
        version_url = application_dict['version_url']
        latest_version = get_version_from_filename(version_url=version_url)
        print(f"get_version_from_filename() · latest_version={latest_version}")
