import pyodbc
import pandas as pd

conexion = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=ComercialAndes;"
    "Trusted_Connection=yes;"
)

tabla = pd.read_sql("SELECT * FROM clientes", conexion)
print(tabla)

conexion.close()
