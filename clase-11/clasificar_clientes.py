import pandas as pd

tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")

def clasificar_cliente(monto):
    if monto >= 90000:
        return "VIP"
    elif monto >= 50000:
        return "Premium"
    else:
        return "Regular"

tabla_clientes["categoria"] = tabla_clientes["monto_compra"].apply(clasificar_cliente)

print(tabla_clientes)



def evaluar_riesgo(sucursal):
    if sucursal == "Sucursal Providencia" or sucursal == "Sucursal Las Condes":
        return "Zona Centro"
    elif sucursal == "Sucursal Concepción" or sucursal == "Sucursal Maipú":
        return "Zona Sur"

tabla_clientes["zona"] = tabla_clientes["sucursal"].apply(evaluar_riesgo)

print(tabla_clientes)
