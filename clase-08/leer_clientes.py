import pandas as pd

tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")

print(tabla_clientes)

print(tabla_clientes.head(2))

print(tabla_clientes.tail(3))

tabla_clientes.info()

