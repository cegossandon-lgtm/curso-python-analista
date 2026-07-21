import yfinance as yf
import pandas as pd
import numpy as np

acciones = ["AAPL", "MSFT", "GOOGL", "AMZN"]

precios = yf.download(acciones, start="2024-01-01", end="2025-01-01")["Close"]

retornos = precios.pct_change()

volatilidad_diaria = retornos.std()
print("Volatilidad diaria:")
print(volatilidad_diaria)

volatilidad_anual = volatilidad_diaria * np.sqrt(252)
print("\nVolatilidad anual:")
print(volatilidad_anual)
