# tests/test_data_collector.py
import pandas as pd
import pytest
from src.data_collector import YahooFinanceFetcher

def test_get_prices():
    """"Basic test for importing data from Yahoo Finance"""
    fetcher = YahooFinanceFetcher()
    tickers = ["AAPL"]
    df = fetcher.get_prices(tickers, "2022-01-01", "2022-01-31")
    print(df)
    assert isinstance(df, pd.DataFrame)
    assert "AAPL" in df.columns
    assert not df.empty
