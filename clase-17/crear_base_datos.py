import sqlite3
import pandas as pd

conexion = sqlite3.connect("clase-17/comercial_andes.db")

tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")

tabla_clientes.to_sql("clientes", conexion, if_exists="replace", index=False)

conexion.close()
