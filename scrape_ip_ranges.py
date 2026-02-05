"""
IP Ranges Scraper for ipdeny.com
This script scrapes the ipdeny.com website and downloads all country IP ranges in .zone format.
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


def create_download_directory(directory_name="ip_zones"):
    """Create a directory to store downloaded zone files."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Created directory: {directory_name}")
    return directory_name


def scrape_zone_files(url="https://www.ipdeny.com/ipblocks/"):
    """
    Scrape the ipdeny.com website and extract all .zone file URLs.

    Args:
        url: The URL to scrape (default: https://www.ipdeny.com/ipblocks/)

    Returns:
        A list of tuples containing (country_code, zone_url)
    """
    print(f"Fetching page: {url}")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    # Find all links that end with .zone
    zone_links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        # Match links to .zone files in the countries directory
        if href.endswith(".zone") and "/countries/" in href:
            # Extract country code from the filename
            match = re.search(r"/([a-z]{2})\.zone$", href)
            if match:
                country_code = match.group(1)
                full_url = urljoin(url, href)
                zone_links.append((country_code, full_url))

    print(f"Found {len(zone_links)} zone files")
    return zone_links


def download_zone_file(country_code, url, directory):
    """
    Download a single zone file.

    Args:
        country_code: Two-letter country code
        url: URL of the zone file
        directory: Directory to save the file

    Returns:
        True if successful, False otherwise
    """
    filename = f"{country_code}.zone"
    filepath = os.path.join(directory, filename)

    try:
        print(f"Downloading {country_code.upper()}... ", end="", flush=True)
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            f.write(response.content)

        file_size = len(response.content)
        print(f"✓ ({file_size:,} bytes)")
        return True

    except requests.RequestException as e:
        print(f"✗ Error: {e}")
        return False


def main():
    """Main function to orchestrate the scraping and downloading process."""
    print("=" * 60)
    print("IP Ranges Scraper for ipdeny.com")
    print("=" * 60)
    print()

    # Create download directory
    download_dir = create_download_directory("ip_zones")
    print()

    # Scrape zone file URLs
    zone_files = scrape_zone_files()

    if not zone_files:
        print("No zone files found. Exiting.")
        return

    print()
    print(f"Starting download of {len(zone_files)} files...")
    print("-" * 60)

    # Download each zone file
    successful = 0
    failed = 0

    for country_code, url in zone_files:
        if download_zone_file(country_code, url, download_dir):
            successful += 1
        else:
            failed += 1

        # small delay between requests
        time.sleep(0.1)

    # Summary
    print("-" * 60)
    print()
    print("Download Summary:")
    print(f"  ✓ Successful: {successful}")
    print(f"  ✗ Failed: {failed}")
    print(f"  Total: {len(zone_files)}")
    print()
    print(f"Files saved to: {os.path.abspath(download_dir)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
