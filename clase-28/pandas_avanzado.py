import pandas as pd

clientes = pd.DataFrame([
    {"nombre": "María Fernanda Rojas", "monto_compra": 45990, "sucursal": "Sucursal Providencia"},
    {"nombre": "Javier Pérez Silva", "monto_compra": 33990, "sucursal": "Sucursal Las Condes"},
    {"nombre": "Ana Torres", "monto_compra": 78500, "sucursal": "Sucursal Concepción"},
    {"nombre": "Carlos Ossandón", "monto_compra": 100500, "sucursal": "Sucursal Maipú"},
])

sucursales_info = pd.DataFrame([
    {"sucursal": "Sucursal Providencia", "region": "Metropolitana"},
    {"sucursal": "Sucursal Las Condes", "region": "Metropolitana"},
    {"sucursal": "Sucursal Concepción", "region": "Biobío"},
    {"sucursal": "Sucursal Maipú", "region": "Metropolitana"},
])

clientes["sucursal"] = clientes["sucursal"].str.strip().str.title()
sucursales_info["sucursal"] = sucursales_info["sucursal"].str.strip().str.title()

tabla_completa = clientes.merge(sucursales_info, on="sucursal")
print(tabla_completa)

tabla = pd.read_excel("clase-22/clientes_limpios.xlsx")

tabla["categoria"] = tabla["monto_compra"].apply(
    lambda monto: "VIP" if monto >= 90000 else "Premium" if monto >= 50000 else "Regular"
)

tabla_dinamica = pd.pivot_table(
    tabla,
    values="monto_compra",
    index="sucursal",
    columns="categoria",
    aggfunc="sum",
    fill_value=0
)

print(tabla_dinamica)

