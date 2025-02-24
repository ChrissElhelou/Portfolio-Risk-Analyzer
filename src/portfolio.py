import numpy as np
import pandas as pd

def calc_daily_earnings(prices: pd.DataFrame) -> pd.DataFrame:
    """Calculate daily percentage returns for the price data."""
    returns = prices.pct_change().dropna()
    return returns
def calc_portfolio_earnings(returns: pd.DataFrame, weights: np.ndarray) -> pd.Series: 
    """Compute the portfolio's daily returns given individual asset returns and weights."""
    portfolio_returns = returns.dot(weights)
    portfolio_returns.name = "PortfolioReturn"
    return portfolio_returns
