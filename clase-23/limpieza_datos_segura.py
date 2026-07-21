import pandas as pd

try:
    tabla = pd.read_excel("clase-20/clientes_sucios.xlsx")
    print(f"Filas antes de limpiar: {len(tabla)}")

    tabla = tabla.drop_duplicates()
    print(f"Filas después de quitar duplicados: {len(tabla)}")

    tabla["sucursal"] = tabla["sucursal"].str.strip()
    tabla["sucursal"] = tabla["sucursal"].str.title()
    tabla["sucursal"] = tabla["sucursal"].replace("Sucursal Maipu", "Sucursal Maipú")

    tabla = tabla.dropna(subset=["monto_compra"])
    print(f"Filas después de quitar nulos en monto_compra: {len(tabla)}")

    tabla.to_excel("clase-23/clientes_limpios.xlsx", index=False)
    print("Archivo limpio exportado correctamente.")

except FileNotFoundError as error:
    print(f"No se encontró el archivo de entrada. Detalle: {error}")

except KeyError as error:
    print(f"Falta una columna esperada en el archivo. Detalle: {error}")

except Exception as error:
    print(f"Ocurrió un error inesperado. Detalle: {error}")


