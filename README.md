# SEC 10-K Filings: Download, Extraction and LLM Insight Generation

A pipeline that downloads companies' annual 10-K filings from SEC EDGAR, extracts structured metadata from them, and sends their text to a language model through the Hugging Face Inference API to generate insights.

The three companies come from deliberately different sectors:
- **Caterpillar (CAT)**: industrial machinery
- **Pfizer (PFE)**: pharmaceuticals
- **Block / Square (SQ)**: fintech

## Pipeline

| Step | Script | What it does |
|---|---|---|
| 1. Download | `download_filings.py` | Fetches 10-K filings for each ticker with `sec_edgar_downloader` |
| 2. Extract | `Extract_data.py` | Parses each filing's SEC header: accession number, submission type, period of report, filing date, company name, CIK, SIC code, IRS number |
| 3. Generate | `LLM_API.py`, `Insight_Generation.py` | Sends filing text to `distilgpt2` through the Hugging Face Inference API and returns generated text |

## Setup

```bash
pip install sec_edgar_downloader requests
```

Set your Hugging Face API token as an environment variable. It is never stored in the code:

```bash
export HF_API_TOKEN=your_token_here        # macOS / Linux
setx HF_API_TOKEN "your_token_here"        # Windows
```

In `download_filings.py`, replace the placeholder email with your own. The SEC's fair-access policy requires one.

## Usage

```bash
python download_filings.py      # 1. download filings into sec_filings/
python Extract_data.py          # 2. print metadata for each filing
python Insight_Generation.py    # 3. generate text with the LLM
```

## Analyse other companies

Edit the `tickers` list in `download_filings.py`:

```python
tickers = ["CAT", "PFE", "SQ"]
```

You can look up ticker symbols on [Yahoo Finance](https://finance.yahoo.com) or [NASDAQ](https://www.nasdaq.com/market-activity/stocks/screener).

## Tech stack

Python, sec-edgar-downloader, Hugging Face Inference API (distilgpt2), requests
