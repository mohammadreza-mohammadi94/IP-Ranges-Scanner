# IP Ranges Scraper

A Python script to scrape and download IP ranges for all countries from [ipdeny.com](https://www.ipdeny.com/ipblocks/) in `.zone` format.

## Features

- 🌍 Downloads IP ranges for all countries
- 📁 Automatically creates organized directory structure
- 📊 Progress tracking with detailed output
- ⚡ Efficient with rate limiting to be server-friendly
- 🛡️ Error handling and retry logic

## Requirements

- Python 3.6+
- Required packages (see `requirements.txt`)

## Installation

1. Clone or download this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Simply run the script:

```bash
python scrape_ip_ranges.py
```

The script will:
1. Create an `ip_zones` directory (if it doesn't exist)
2. Scrape the ipdeny.com website for all country zone files
3. Download each `.zone` file to the `ip_zones` directory
4. Display progress and summary statistics

## Output

All downloaded `.zone` files will be saved in the `ip_zones` directory with the naming format:
- `us.zone` - United States
- `gb.zone` - United Kingdom
- `cn.zone` - China
- etc.

Each file contains IP ranges in CIDR format for the respective country.

## Example Output

```
============================================================
IP Ranges Scraper for ipdeny.com
============================================================

Created directory: ip_zones

Fetching page: https://www.ipdeny.com/ipblocks/
Found 249 zone files

Starting download of 249 files...
------------------------------------------------------------
Downloading AF... ✓ (2,150 bytes)
Downloading AX... ✓ (51 bytes)
Downloading AL... ✓ (3,670 bytes)
...
------------------------------------------------------------

Download Summary:
  ✓ Successful: 249
  ✗ Failed: 0
  Total: 249

Files saved to: C:\...\IP-Ranges\ip_zones
============================================================
```

## Notes

- The script includes a small delay (0.1s) between requests to be respectful to the server
- Files are downloaded from: `https://www.ipdeny.com/ipblocks/data/countries/`
- Zone files are updated regularly on the source website

## License

This is a simple scraper tool. Please respect ipdeny.com's [usage limits](https://www.ipdeny.com/usagelimits.php) and [copyright policy](https://www.ipdeny.com/copyright.php).
