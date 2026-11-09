# Diverse-Company-10K-Filings-Analysis
## Installation and Usage

Before running the analysis, you need to download the necessary 10-K filings. This project uses the `sec_edgar_downloader` Python package to automate the download of these filings from the SEC EDGAR database.

### Prerequisites

- Python 
- `sec_edgar_downloader` package (installable via pip)

### Setup

1. Clone this repository to your local machine using:
git clone https://github.com/NadaNabil07/Diverse-Company-10K-Filings-Analysis/tree/main

2. Install the required Python package by running:
`pip install sec_edgar_downloader`
## Project Rationale

In this project we have  choosen companies to download 10 K filings to go for a mix, like Caterpillar Inc., Pfizer Inc. And Square, Inc. Caterpillar gives you a peek into machinery Pfizer shows you the pharmaceutical world and Square dives into the fintech scene. By covering industries, market sizes and locations you can get a grasp of diverse sectors along, with their unique hurdles and chances.

### Customizing the Analysis for Other Companies

If you wish to analyze different companies, you can replace the tickers in the `tickers` list with the ticker symbols of your target companies. To find the ticker symbol for a specific company, you can use financial websites such as:

- [Yahoo Finance](https://finance.yahoo.com)
- [NASDAQ](https://www.nasdaq.com/market-activity/stocks/screener)
- [Bloomberg](https://www.bloomberg.com/markets/stocks)

Simply search for the company name on these websites, and the corresponding ticker symbol will be displayed. For example, searching for "Apple Inc." on Yahoo Finance will show its ticker symbol as "AAPL".

### Updating the Ticker List

Once you have the ticker symbols for the companies you are interested in, update the `tickers` list in the `download_filings.py` script:

```python
# Define the tickers for your target companies
tickers = ["CAT", "PFE", "SQ"]  # Replace with your chosen companies
```
### Downloading SEC Filings
Run the `download_filings.py` file and notice the folowing : 
Replace `your_email@example.com` with your actual email address before running the script. This email is required by the SEC's Fair Access Rule.[Source](https://www.sec.gov/os/webmaster-faq#code-support)

To run the script, execute it in your terminal:
`python download_filings.py`
This will download all the 10-K filings for the specified companies and years into the sec_filings directory.
# task 1.2 
### step 1 : DMake sure to adjust the paths according to your Python installation and script location.ata Cleaning and Extraction 
Make sure to adjust the paths according to your Python installation and script location.
# Metadata Extractor

This script will process each text file in the specified directory, extracting and printing the metadata to the console. The output includes:

- `<SEC-DOCUMENT>`: The name and date of the document.
- `<SEC-HEADER>`: The header information of the document.
- ACCESSION NUMBER: The unique identifier for the submission.
- CONFORMED SUBMISSION TYPE: The type of report, e.g., 10-K.
- PUBLIC DOCUMENT COUNT: The number of documents included in the submission.
- CONFORMED PERIOD OF REPORT: The period that the report covers.
- FILED AS OF DATE: The date the document was filed.
- COMPANY DATA: Information about the company, including the conformed name, central index key, standard industrial classification, and IRS number.

## Usage
1. Navigate to the directory where the script is located.
3. Run the script `Extract_data.py` with the specified directory containing the text files as an argument.

## Step 2: Text Generation with Hugging Face API

In this stage we make use of the Hugging Face API to carry out text generation tasks using the information extracted from SEC EDGAR 10 K filings. We utilize the `distilgpt2` model, which's a compact version of the GPT 2 model designed for quicker inference, with minimal impact on performance.

To access the Hugging Face API you will need to acquire an API key. Follow these steps to obtain your API key;

1. Visit the [Hugging Face website](https;//huggingface.co/).
2. Create an account if you are not already registered.
3. Once you are logged in navigate, to your account settings.
4. Locate the API keys section and generate an API key.


### services provide plans or trial periods, for utilizing LLM APIs;

 **Hugging Face**; Offers a tier with restricted usage, ideal for development and small scale applications.
 **OpenAI**; Grants access to GPT 3 and GPT 4 models providing users with credits upon registration.
 **AI21 Studio**; Allows access to their Jurassic 1 LLM offering credits that renew every month.
 **Cohere**; Provides a tier with an amount of complimentary credits suitable, for various NLP tasks.

### Implementation

A Python script `LLM_API.py` was developed to send prompts to the API and receive generated text. The script handles API responses and prints out the generated text or error messages accordingly.

### Usage

To run the script, use the following command in the terminal:

```powershell
 python LLM_API.py
```
## Insights 
To generate insights run the Python script named Insight_Generation.py.

Why These Insights Matter to Users
These insights are valuable, for investors, analysts and stakeholders as they help in making informed investment decisions understanding company performance and forecasting trends.

Visuals
You can find the representations, in the 'visualizations folder. They present the insights graphically simplifying data for comprehension.

Wrap up
This project offers a set of tools to analyze and visualize details extracted from 10 K filings. It assists stakeholders in their decision making processes.

Note : Did not finished the project due to the final exams , but for sure back completing it in a perfect way because it is so amzing project 
contact me : nada.nabi.soudi@gamil.com 


