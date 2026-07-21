import pandas as pd

tabla = pd.read_excel("clase-20/clientes_sucios.xlsx")
print(f"Filas antes de limpiar: {len(tabla)}")

# Paso 1: eliminar duplicados verdaderos
tabla = tabla.drop_duplicates()
print(f"Filas después de quitar duplicados: {len(tabla)}")

# Paso 2: estandarizar texto de sucursal
tabla["sucursal"] = tabla["sucursal"].str.strip()
tabla["sucursal"] = tabla["sucursal"].str.title()
tabla["sucursal"] = tabla["sucursal"].replace("Sucursal Maipu", "Sucursal Maipú")
print(tabla["sucursal"].unique())

# Paso 3: eliminar filas sin monto_compra
tabla = tabla.dropna(subset=["monto_compra"])
print(f"Filas después de quitar nulos en monto_compra: {len(tabla)}")

# Exportar tabla limpia
tabla.to_excel("clase-22/clientes_limpios.xlsx", index=False)
print("Archivo limpio exportado correctamente.")

