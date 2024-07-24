import yfinance as yf

stock_data = yf.Ticker('AMZN')
stock_split = stock_data.splits
print(stock_split)