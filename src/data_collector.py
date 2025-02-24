# src/data_fetcher.py
import yfinance as yf
import pandas as pd

class YahooFinanceFetcher:
    """Fetches historical market data from Yahoo Finance using yfinance."""
    
    def get_prices(self, tickers, start_date=None, end_date=None):
        """Fetches historical market data for given tickers and dates"""
        try:
            data = yf.download(tickers, start=start_date, end=end_date, progress=False)
            df = data['Adj Close']
        except Exception as e:
            raise RuntimeError(f"Data collection failed due to: {e}")
        
        df.dropna(inplace=True) #If there are missing values, remove them
        return df
