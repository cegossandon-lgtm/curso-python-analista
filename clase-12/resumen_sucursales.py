import pandas as pd

tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")

ventas_por_sucursal = tabla_clientes.groupby("sucursal")["nombre"].count()

print(ventas_por_sucursal)

