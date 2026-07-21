import pandas as pd
import matplotlib.pyplot as plt

tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")

ventas_por_sucursal = tabla_clientes.groupby("sucursal")["monto_compra"].sum()

ventas_por_sucursal.plot(kind="bar")

plt.title("Ventas Totales por Sucursal - Comercial Andes S.A.")
plt.xlabel("Sucursal")
plt.ylabel("Monto Total ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("clase-16/ventas_por_sucursal.png")

plt.show()


tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")


def clasificar_cliente(monto):
    if monto >= 90000:
        return "VIP"
    elif monto >= 50000:
        return "Premium"
    else:
        return "Regular"

tabla_clientes["categoria"] = tabla_clientes["monto_compra"].apply(clasificar_cliente)

cantidad_clientes_por_categoria = tabla_clientes.groupby("categoria")["monto_compra"].count()

cantidad_clientes_por_categoria.plot(kind="bar")

plt.title("Cantidad de Clientes por Categoria - Comercial Andes S.A.")
plt.xlabel("Categoría")
plt.ylabel("Cantidad de clientes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("clase-16/ventas_por_sucursal_2.png")


plt.show()
