import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Apple Stock Price App
         
Shown are stock closing price and volume of Apple!
         
""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1mo', start='2010-1-1', end='2023-1-1')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)