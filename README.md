# Portfolio Risk Analyzer (VaR Calculation)

Python tool to calculate Value-at-Risk (VaR) for financial portfolios through three different methods: Historical Simulation, Parametric (Variance-Covariance), and Monte Carlo Simulation. Fetches real-time market data from Yahoo Finance and generates risk visualizations.

## Features

- **Three VaR Calculation Methods**
  - Historical Simulation
  - Parametric (Normal Distribution)
  - Monte Carlo Simulation
- Real-time data fetching from Yahoo Finance via `yfinance`
- Portfolio return calculations
- Matplotlib visualizations of risk metrics
- Comprehensive unit tests (pytest)t

## Installation

### Prerequisites
- Python 3.9+
- pip

1. Clone the repository:
```bash
git clone https://github.com/your-username/Portfolio-Risk-Analyzer.git
cd Portfolio-Risk-Analyzer
