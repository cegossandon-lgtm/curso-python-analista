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


retorno_total = (precios.iloc[-1] / precios.iloc[0]) - 1
print("Retorno total del período:")
print(retorno_total)

correlacion = retornos.corr()
print("\nMatriz de correlación:")
print(correlacion)


pesos = np.array([0.25, 0.25, 0.25, 0.25])

retorno_portafolio = np.sum(retorno_total * pesos)
print(f"\nRetorno total del portafolio combinado: {retorno_portafolio:.4f}")


matriz_covarianza = retornos.cov() * 252

varianza_portafolio = np.dot(pesos.T, np.dot(matriz_covarianza, pesos))
volatilidad_portafolio = np.sqrt(varianza_portafolio)

print(f"\nVolatilidad anual del portafolio combinado: {volatilidad_portafolio:.4f}")

