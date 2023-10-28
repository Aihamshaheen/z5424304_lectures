"""yf_example3.py

Module to download Qantas stock price data for a given year and save it in a CSV file.
"""

import os
import toolkit_config as cfg
from yf_example2 import yf_prc_to_csv

def qan_prc_to_csv(year):
    """Download Qantas stock prices for a given year into a CSV file.

    The CSV file will be named qan_prc_YYYY.csv, where YYYY is the year.
    The file will be saved in the data folder specified in toolkit_config.py.
    """
    # Create start and end dates for the specified year
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    # Ticker symbol for Qantas
    tic = 'QAN.AX'

    # Create the name of the output CSV file
    output_file_name = f"qan_prc_{year}.csv"

    # Create the path to save the CSV file inside the data folder
    output_file_path = os.path.join(cfg.DATADIR, output_file_name)

    # Download and save the stock price data
    yf_prc_to_csv(tic, output_file_path, start=start_date, end=end_date)

if __name__ == "__main__":
    # Example: Download Qantas stock price data for the year 2020
    qan_prc_to_csv(year=2020)
