from sec_edgar_downloader import Downloader
import os

# Define the directory where you want to save the filings
download_directory = "sec_filings"

# Your email address (as required by the SEC's Fair Access Rule)
your_email = "your_email@example.com"  # Replace with your actual email address

# Create the directory if it does not exist
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Initialize a downloader instance with your email address
dl = Downloader(download_directory, your_email)

# Define the tickers and the range of years
tickers = ["CAT", "PFE", "SQ"]  # Replace with your chosen companies
years = range(1995, 2024)

# Download 10-K filings for each ticker and year
for ticker in tickers:
    for year in years:
        try:
            # Download the 10-K filings
            dl.get("10-K", ticker, after=f"{year}-01-01", before=f"{year}-12-31")
            print(f"Successfully downloaded 10-K for {ticker} for the year {year}")
        except Exception as e:
            print(f"An error occurred for {ticker} for the year {year}: {e}")

print("Download complete.")
