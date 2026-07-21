import pandas as pd

tabla = pd.read_excel("clase-20/clientes_sucios.xlsx")

print(f"Total de filas: {len(tabla)}")


nulos_por_columna = tabla.isnull().sum()
print(nulos_por_columna)

cantidad_duplicados = tabla.duplicated().sum()
print(f"Filas duplicadas: {cantidad_duplicados}")

sucursales_unicas = tabla["sucursal"].unique()
print(sucursales_unicas)


filas_duplicadas = tabla[tabla.duplicated(keep=False)]
print(filas_duplicadas.sort_values("nombre").head(10))

