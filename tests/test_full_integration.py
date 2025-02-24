# tests/test_full_integration.py
import numpy as np
import pandas as pd
import pytest
from src.data_collector import YahooFinanceFetcher
from src.portfolio import calc_daily_earnings, calc_portfolio_earnings
from src.VaR_calculator import historical_var, parameter_var, monte_carlo_VaR

def test_full_integration():
    dates = pd.date_range("2022-01-01", periods=10)
    data = {
        "AAPL": np.linspace(150, 155, 10),
        "MSFT": np.linspace(300, 310, 10),
        "GOOG": np.linspace(2700, 2720, 10)
    }
    prices = pd.DataFrame(data, index=dates)
    returns_df = calc_daily_earnings(prices)
    weights = np.array([0.5, 0.3, 0.2])
    portfolio_returns = calc_portfolio_earnings(returns_df, weights)
    
    var_hist = historical_var(portfolio_returns, confidence=0.95)
    var_param = parameter_var(portfolio_returns, confidence=0.95)
    var_mc = monte_carlo_VaR(returns_df, weights, confidence=0.95, simulations=1000)
    
    assert var_hist > 0
    assert var_param > 0
    assert var_mc > 0
