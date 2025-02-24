# tests/test_var_calculator.py
import numpy as np
import pandas as pd
import pytest
from src.VaR_calculator import historical_var, parameter_var, monte_carlo_VaR

def test_historical_var():
    returns = pd.Series(np.linspace(-0.05, 0.05, 101))
    var_value = historical_var(returns, confidence=0.95)
    np.testing.assert_almost_equal(var_value, 0.045, decimal=2)

def test_parametric_var():
    np.random.seed(42)
    returns = pd.Series(np.random.normal(0, 0.02, 1000))
    var_value = parameter_var(returns, confidence=0.95)
    expected_var = 1.645 * 0.02
    np.testing.assert_almost_equal(var_value, expected_var, decimal=1)

def test_monte_carlo_var():
    np.random.seed(42)
    data = {
        "AAPL": np.random.normal(0, 0.01, 1000),
        "MSFT": np.random.normal(0, 0.015, 1000)
    }
    returns_df = pd.DataFrame(data)
    weights = np.array([0.5, 0.5])
    var_value = monte_carlo_VaR(returns_df, weights, confidence=0.95, simulations=5000)
    assert var_value > 0
    assert var_value < 0.05
