import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
# Simple Stock Price App

Shown are te stock closing prices and volume of Google! 

""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker 
tickerDF = tickerData.history(period='1d', start='2010-1-1', end='2021-4-10')
#open High LowClose Volume Dividends StockSplits

st.write("""
---
# GOOGLE
""")
st.write("""
## Closing Price 
""")
st.line_chart(tickerDF.Close)
st.write("""
## Volume Price 
""")
st.line_chart(tickerDF.Volume)


#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker 
tickerDF = tickerData.history(period='1d', start='2010-1-1', end='2021-4-10')
#open High LowClose Volume Dividends StockSplits

st.write("""
---
# APPLE
""")
st.write("""
## Closing Price 
""")
st.line_chart(tickerDF.Close)
st.write("""
## Volume Price 
""")
st.line_chart(tickerDF.Volume)
=======
import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
# Simple Stock Price App

Shown are te stock closing prices and volume of Google! 

""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker 
tickerDF = tickerData.history(period='1d', start='2010-1-1', end='2021-4-10')
#open High LowClose Volume Dividends StockSplits

st.write("""
## Closing Price 
""")
st.line_chart(tickerDF.Close)
st.write("""
## Volume Price 
""")
st.line_chart(tickerDF.Volume)
>>>>>>> 28ef6be089159e4f5c47bb935c760a3a8561f11f
