import pandas as pd

tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")

tabla_clientes["monto_con_descuento"] = tabla_clientes["monto_compra"] * 0.9

tabla_clientes["monto_con_descuento"] = tabla_clientes["monto_con_descuento"].round(0)

print(tabla_clientes)


tabla_clientes["impuesto_19"] = tabla_clientes["monto_compra"]*0.19
tabla_clientes["impuesto_19"] = tabla_clientes["impuesto_19"].round(0)

print(tabla_clientes)
