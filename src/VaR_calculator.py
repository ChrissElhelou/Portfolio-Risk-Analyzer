# src/var_calculator.py
import numpy as np
import scipy.stats as stats
import pandas as pd

def historical_var(portfolio_returns: pd.Series, confidence: float = 0.95) -> float:
    """Computes and returns VaR using the Historical Simulation method as a percentage of the portfolio."""
    if len(portfolio_returns) == 0:
        raise ValueError("Returns series is empty.")
    alpha = 1 - confidence
    var_threshold = -np.percentile(portfolio_returns, 100 * alpha)
    return var_threshold

def parameter_var(portfolio_returns: pd.Series, confidence: float = 0.95) -> float:
    """Computes VaR by using the Variance-Covarianc method by assuming normally distributed returns."""
    if len(portfolio_returns) == 0:
        raise ValueError("Returns series is empty.")
    mu = portfolio_returns.mean()
    sigma = portfolio_returns.std(ddof=0)
    alpha = 1 - confidence
    z = stats.norm.ppf(alpha)
    var_threshold = -mu + z * sigma
    return var_threshold

def monte_carlo_VaR(asset_returns_df: pd.DataFrame, weights: np.ndarray, confidence: float = 0.95, simulations: int = 10000) -> float:
    """Computes VaR using Monte Carlo simulation based on asset returns."""
    if asset_returns_df.empty:
        raise ValueError("Asset returns DataFrame is empty.")
    weights = np.array(weights)
    mu_vec = asset_returns_df.mean().values
    cov_matrix = asset_returns_df.cov().values
    simulated_returns = np.random.multivariate_normal(mu_vec, cov_matrix, size=simulations)
    portfolio_simulated = simulated_returns.dot(weights)
    alpha = 1 - confidence
    var_threshold = -np.percentile(portfolio_simulated, 100 * alpha)
    return var_threshold
