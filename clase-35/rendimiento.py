import pandas as pd
import numpy as np
import time

np.random.seed(42)

n_filas = 500000

tabla = pd.DataFrame({
    "id_cliente": range(1, n_filas + 1),
    "monto_compra": np.random.randint(10000, 150000, size=n_filas)
})

print(f"Filas generadas: {len(tabla)}")



def clasificar_monto(monto):
    if monto >= 90000:
        return "VIP"
    elif monto >= 50000:
        return "Premium"
    else:
        return "Regular"

inicio = time.time()

categorias_loop = []
for i in range(len(tabla)):
    monto = tabla.iloc[i]["monto_compra"]
    categorias_loop.append(clasificar_monto(monto))

fin = time.time()
print(f"Tiempo con loop manual (.iloc): {fin - inicio:.2f} segundos")

inicio = time.time()

categorias_apply = tabla["monto_compra"].apply(clasificar_monto)

fin = time.time()
print(f"Tiempo con .apply(): {fin - inicio:.2f} segundos")


inicio = time.time()

categorias_vectorizado = np.select(
    [tabla["monto_compra"] >= 90000, tabla["monto_compra"] >= 50000],
    ["VIP", "Premium"],
    default="Regular"
)

fin = time.time()
print(f"Tiempo con np.select() (vectorizado puro): {fin - inicio:.4f} segundos")