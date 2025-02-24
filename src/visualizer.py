# src/visualizer.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_return_distribution(portfolio_returns: pd.Series, var_value: float, filename: str = "return_distribution.png"):
    """Plots a histogram of the portfolio returns with the VaR threshold marked in the plots"""
    plt.figure(figsize=(6,4))
    plt.hist(portfolio_returns, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    # VaR is a loss (e.g., 0.04 means a 4% loss), so mark -var_value
    plt.axvline(x=-var_value, color='red', linestyle='--', linewidth=2,
                label=f"VaR ({var_value:.2%})")
    plt.title("Portfolio Return Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def compute_rolling_var(portfolio_returns: pd.Series, window: int = 250, confidence: float = 0.95) -> pd.Series:
    """Computes a rolling historical VaR over a specified window."""
    rolling_vars = portfolio_returns.rolling(window=window).apply(
        lambda x: -np.percentile(x, 100 * (1 - confidence)), raw=True)
    return rolling_vars.dropna()

def plot_rolling_var(rolling_var: pd.Series, filename: str = "rolling_var.png"):
    """Plots the time series vs the rolling VaR values."""
    plt.figure(figsize=(8,5))
    plt.plot(rolling_var.index, rolling_var.values, color='blue', linewidth=2)
    plt.title("Rolling VaR over Time")
    plt.xlabel("Date")
    plt.ylabel("VaR (as fraction of portfolio value)")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
