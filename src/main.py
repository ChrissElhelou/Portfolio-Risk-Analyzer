# src/main.py
import numpy as np
import pandas as pd
from data_collector import YahooFinanceFetcher
from portfolio import calc_daily_earnings, calc_portfolio_earnings
from VaR_calculator import historical_var, parameter_var, monte_carlo_VaR
from visualizer import plot_return_distribution, compute_rolling_var, plot_rolling_var

def main():
    # Configuration
    tickers = ["NVDA", "MSFT", "GOOG"]
    weights = [0.5, 0.3, 0.2]
    start_date = "2020-01-01"
    end_date = "2024-01-01"
    confidence = 0.95

    # Fetch historical price data
    fetcher = YahooFinanceFetcher()
    prices = fetcher.get_prices(tickers, start_date, end_date)
    
    # Calculate daily returns
    returns_df = calc_daily_earnings(prices)
    
    # Compute portfolio returns using provided weights
    portfolio_returns = calc_portfolio_earnings(returns_df, np.array(weights))
    
    # Compute VaR using three methods
    var_hist = historical_var(portfolio_returns, confidence)
    var_param = parameter_var(portfolio_returns, confidence)
    var_mc = monte_carlo_VaR(returns_df, np.array(weights), confidence, simulations=10000)
    
    print(f"95% VaR (Historical): {var_hist:.2%}")
    print(f"95% VaR (Parametric): {var_param:.2%}")
    print(f"95% VaR (Monte Carlo): {var_mc:.2%}")
    
    # Generate and save risk visualizations
    plot_return_distribution(portfolio_returns, var_hist, filename="return_distribution.png")
    rolling_var = compute_rolling_var(portfolio_returns, window=250, confidence=confidence)
    plot_rolling_var(rolling_var, filename="rolling_var.png")

if __name__ == "__main__":
    main()
