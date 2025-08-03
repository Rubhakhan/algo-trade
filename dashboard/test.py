import sys, os
sys.path.insert(0, os.path.abspath("."))

from analytics.load_data import load_stock_data
from analytics.statistics import add_moving_average, add_volatility
#print(load_stock_data)
#print(add_moving_average)