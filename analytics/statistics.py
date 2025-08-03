import pandas as pd
from load_data import load_stock_data

def add_moving_average(df, window=20):
    df[f"MA_{window}"] = df['Close'].rolling(window=window).mean()
    return df

def add_volatility(df, window=20):
    df[f"Volatility_{window}"] = df['Close'].rolling(window=window).std()
    return df

if __name__ == "__main__":
    df = load_stock_data("AAPL")
    df = add_moving_average(df, window=20)
    df = add_volatility(df, window=20)
    print(df.tail())

import matplotlib.pyplot as plt

df[['Close', 'MA_20']].plot(figsize=(12,6), title='AAPL Close Price and 20-day MA')
plt.show()

df['Volatility_20'].plot(figsize=(12,6), title='AAPL 20-day Rolling Volatility')
plt.show()
