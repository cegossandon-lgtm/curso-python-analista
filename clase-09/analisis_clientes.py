import pandas as pd

tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")

nombres_y_montos = tabla_clientes[["nombre", "monto_compra"]]

print(nombres_y_montos)

clientes_alto_monto = tabla_clientes[tabla_clientes["monto_compra"] > 50000]

print(clientes_alto_monto)


clientes_las_condes = tabla_clientes[tabla_clientes["sucursal"] == "Sucursal Las Condes"]

print(clientes_las_condes)

nombre_y_montos_sucursal_las_condes = clientes_las_condes[["nombre", "monto_compra"]]

nombre_y_montos_sucursal_las_condes_ = tabla_clientes[tabla_clientes["sucursal"] == "Sucursal Las Condes"][["nombre", "monto_compra"]]


print(nombre_y_montos_sucursal_las_condes)

print(nombre_y_montos_sucursal_las_condes_)

