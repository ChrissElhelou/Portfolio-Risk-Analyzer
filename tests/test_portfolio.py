# tests/test_portfolio.py
import numpy as np
import pandas as pd
import pytest
from src.portfolio import calc_daily_earnings, calc_portfolio_earnings

def test_calculate_daily_returns():
    dates = pd.date_range("2022-01-01", periods=5)
    data = {"AAPL": [150, 152, 151, 153, 154],
            "MSFT": [300, 305, 303, 307, 310]}
    prices = pd.DataFrame(data, index=dates)
    returns = calc_daily_earnings(prices)
    assert returns.shape[0] == 4
    assert "AAPL" in returns.columns

def test_calculate_portfolio_returns():
    data = {"AAPL": [0.01, 0.02, -0.01, 0.00],
            "MSFT": [0.02, 0.01, 0.03, -0.01]}
    returns = pd.DataFrame(data)
    weights = np.array([0.6, 0.4])
    portfolio_ret = calc_portfolio_earnings(returns, weights)
    assert len(portfolio_ret) == len(returns)
