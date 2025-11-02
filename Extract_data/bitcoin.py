import yfinance as yf

btc = yf.Ticker("BTC-USD")

# Current price
print(btc.info['regularMarketPrice'])

# Fetch 1-minute data for the last 1 hour
#data_1min = yf.download(tickers="BTC-USD", period="1d", interval="1h")
data_1d = btc.history(period="1d", interval="1h")

#data_1min.to_csv('data_1min.csv', index=True)
data_1d.to_csv('data_1d.csv', index=True)
#print(data.tail())
