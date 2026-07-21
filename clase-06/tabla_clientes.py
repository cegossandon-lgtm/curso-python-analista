cliente_1 = {"nombre": "María Fernanda Rojas", "monto_compra": 45990, "sucursal": "Sucursal Providencia"}
cliente_2 = {"nombre": "Javier Pérez Silva", "monto_compra": 33990, "sucursal": "Sucursal Las Condes"}
cliente_3 = {"nombre": "Ana Torres", "monto_compra": 78500, "sucursal": "Sucursal Concepción"}

clientes = [cliente_1, cliente_2, cliente_3]


for cliente in clientes:
    print(f"Cliente: {cliente['nombre']},Monto: ${cliente['monto_compra']},Sucursal: {cliente['sucursal']}")
