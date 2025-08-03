import pandas as pd
import os

def load_stock_data(ticker, period="2y", interval="1d", data_dir="data"):
    file_path = os.path.join(data_dir, f"{ticker}_{period}_{interval}.csv")
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    return df

if __name__ == "__main__":
    df = load_stock_data("AAPL")
    print(df.head())
    