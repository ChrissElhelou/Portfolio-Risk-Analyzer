from setuptools import setup, find_packages

setup(
    name="portfolio_risk_analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "yfinance",
        "pandas",
        "numpy",
        "scipy",
        "matplotlib",
        "pytest",
    ],
)