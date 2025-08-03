import sys
import os

# === PATH FIX: Add project root so we can import analytics modules ===
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from analytics.load_data import load_stock_data
from analytics.statistics import add_moving_average, add_volatility

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Algo Trading Dashboard", layout="wide")
st.title("Algo Trading Dashboard")

# ---- SIDEBAR FOR USER INPUT ----
st.sidebar.header("User Options")
ticker = st.sidebar.text_input("Enter stock ticker (e.g., AAPL, MSFT):", value="AAPL")
period = st.sidebar.selectbox("Data Period", options=["1y", "2y", "5y"], index=1)
interval = st.sidebar.selectbox("Interval", options=["1d", "1wk"], index=0)
ma_window = st.sidebar.slider("Moving Average Window", min_value=5, max_value=50, value=20)
vol_window = st.sidebar.slider("Volatility Window", min_value=5, max_value=50, value=20)

# ---- LOAD AND PROCESS DATA ----
try:
    df = load_stock_data(ticker, period=period, interval=interval)
    df = add_moving_average(df, window=ma_window)
    df = add_volatility(df, window=vol_window)
    st.success(f"Loaded data for {ticker} ({period}, {interval})")
except FileNotFoundError:
    st.error(f"Data file not found for {ticker} ({period}, {interval}). Please fetch data first using your fetch script!")
    st.stop()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

# ---- DISPLAY CHARTS ----
st.subheader(f"{ticker} Close Price with {ma_window}-Day Moving Average")
st.line_chart(df[['Close', f'MA_{ma_window}']])

st.subheader(f"{ticker} {vol_window}-Day Rolling Volatility")
st.line_chart(df[f'Volatility_{vol_window}'])

# ---- RAW DATA TABLE ----
with st.expander("Show Raw Data Table"):
    st.dataframe(df.tail(50))

# ---- OPTIONAL: DISPLAY PROJECT ROOT (for debug) ----
# st.write("Project root:", project_root)
