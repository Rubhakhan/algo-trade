import yfinance as yf
import pandas as pd
import os

def fetch_and_save(ticker, period="2y", interval="1d", save_dir="data"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, f"{ticker}_{period}_{interval}.csv")
    df.to_csv(file_path)
    print(f"Saved {ticker} data to {file_path}")
    return df

if __name__ == "__main__":
    # Example: Download Apple and Microsoft data for last 2 years, daily
    fetch_and_save("AAPL")
    fetch_and_save("MSFT")