import sqlite3
import pandas as pd

conexion = sqlite3.connect("clase-17/comercial_andes.db")

resultado = pd.read_sql("SELECT * FROM clientes", conexion)

print(resultado)

resultado_filtrado = pd.read_sql("SELECT nombre, monto_compra FROM clientes WHERE monto_compra > 50000", conexion)

print(resultado_filtrado)

conexion.close()

