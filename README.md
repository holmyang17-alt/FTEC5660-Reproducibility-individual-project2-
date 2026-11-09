# FTEC5660 Reproducibility: TradingAgents

This repository contains my reproducibility work for the TradingAgents framework. It reproduces the single-stock analysis for GOOGL.

## Prerequisites

- Python 3.10+
- A valid DeepSeek API Key

## Installation

1. Clone the repository:
git clone https://github.com/holmyang17-alt/FTEC5660-Reproducibility.git

2. Enter the directory:
cd FTEC5660-Reproducibility

3. Create a virtual environment:
python3 -m venv .venv

4. Activate the environment:
source .venv/bin/activate

5. Install dependencies:
pip install -r requirements.txt

6. Add your API key to a .env file:
DEEPSEEK_API_KEY=your_deepseek_api_key_here

## Running the Code

Run the analysis script:
python test_run.py

## Modification Made

1. Switched all data vendors to yfinance: The default configuration failed because Finnhub is not implemented for get_news and get_stock_data. Using yfinance resolves the "Vendor not available" error.

2. Updated the analysis date to 2026-11-09: The initial run on 2025-05-01 resulted in "data withheld" errors. Updating to the current date ensures all real-time news and fundamental data are fetched.

3. Increased debate rounds: max_debate_rounds was increased from 1 to 2 to observe whether deeper multi-agent discussion changes the final trading decision.

Note: The .env file is included in .gitignore and no API keys are committed to this repository.
