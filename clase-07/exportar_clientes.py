import pandas as pd

cliente_1 = {"nombre": "María Fernanda Rojas", "monto_compra": 45990, "sucursal": "Sucursal Providencia"}
cliente_2 = {"nombre": "Javier Pérez Silva", "monto_compra": 33990, "sucursal": "Sucursal Las Condes"}
cliente_3 = {"nombre": "Ana Torres", "monto_compra": 78500, "sucursal": "Sucursal Concepción"}
cliente_4 = {"nombre": "Carlos Ossandón", "monto_compra": 100500, "sucursal": "Sucursal Maipú"}


clientes = [cliente_1, cliente_2, cliente_3, cliente_4]

tabla_clientes = pd.DataFrame(clientes)


print(tabla_clientes)

tabla_clientes.to_excel("clase-07/clientes_comercial_andes.xlsx", index=False)

