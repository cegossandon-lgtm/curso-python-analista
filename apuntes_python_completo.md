# Apuntes de Python — Referencia Completa
### De cero a automatización financiera con Python (35 clases)

Este documento resume todo lo aprendido, organizado por tema, con código comentado para consultar rápido. Todo el código real y probado está en: `github.com/carlosguzmanossandon/curso-python-analista`

---

## ÍNDICE

1. [Fundamentos de Python](#1-fundamentos-de-python)
2. [Pandas — lo básico](#2-pandas--lo-básico)
3. [Automatización (correos, fechas, gráficos, SQL básico)](#3-automatización)
4. [Limpieza de datos reales](#4-limpieza-de-datos-reales)
5. [Manejo de errores (try/except)](#5-manejo-de-errores-tryexcept)
6. [Programación de tareas (schedule)](#6-programación-de-tareas-schedule)
7. [Jupyter Notebook](#7-jupyter-notebook)
8. [Programación Orientada a Objetos (POO)](#8-programación-orientada-a-objetos-poo)
9. [Pandas avanzado (merge, pivot_table, lambda)](#9-pandas-avanzado)
10. [Git y GitHub](#10-git-y-github)
11. [Proyecto financiero: NumPy + yfinance](#11-proyecto-financiero-numpy--yfinance)
12. [SQL Server real (pyodbc)](#12-sql-server-real-pyodbc)
13. [APIs externas (requests)](#13-apis-externas-requests)
14. [Rendimiento con datos masivos](#14-rendimiento-con-datos-masivos)

---

## 1. FUNDAMENTOS DE PYTHON

### Variables y tipos de datos
```python
nombre = "Carlos"          # str (texto)
edad = 30                  # int (entero)
monto = 45990.50           # float (decimal)
es_vip = True              # bool (verdadero/falso)

# f-strings: forma de insertar variables dentro de un texto
print(f"Hola {nombre}, tu monto es {monto}")
```

### Listas
```python
clientes = ["María", "Javier", "Ana"]
clientes[0]                # acceso por índice, empieza en 0 -> "María"
clientes[-1]                # el último elemento -> "Ana"
len(clientes)               # cantidad de elementos -> 3
clientes.append("Carlos")   # agrega un elemento al final
```

### Bucle for
```python
for cliente in clientes:
    print(cliente)
# recorre cada elemento de la lista, uno por uno; la variable "cliente"
# recibe el VALOR, no el índice.

for i in range(5):
    print(i)
# range(5) genera 0,1,2,3,4 -> útil para repetir algo N veces exactas.
```

### Diccionarios
```python
cliente = {"nombre": "María", "monto_compra": 45990}
cliente["nombre"]           # acceso por clave -> "María"

# Lista de diccionarios = una "tabla" en Python puro
clientes = [
    {"nombre": "María", "monto": 45990},
    {"nombre": "Javier", "monto": 33990},
]
```

### Condicionales y funciones
```python
def clasificar_cliente(monto):
    if monto >= 90000:
        return "VIP"
    elif monto >= 50000:
        return "Premium"
    else:
        return "Regular"
# El orden importa: la condición más exigente siempre va primero.
```

### Lambda (función corta, de un solo uso)
```python
clasificar = lambda monto: "VIP" if monto >= 90000 else "Regular"
# Útil dentro de .apply() cuando la lógica es simple y se usa una sola vez.
# Para lógica reutilizada en varios lugares, mejor usar def.
```

---

## 2. PANDAS — LO BÁSICO

### Crear, leer y escribir
```python
import pandas as pd

tabla = pd.DataFrame(lista_de_diccionarios)   # lista de dicts -> tabla
tabla.to_excel("archivo.xlsx", index=False)   # index=False evita columna extra
tabla = pd.read_excel("archivo.xlsx")         # leer un Excel
tabla = pd.read_csv("archivo.csv")            # leer un CSV (mismo patrón)

tabla.head(3)     # primeras 3 filas
tabla.tail(3)      # últimas 3 filas
tabla.info()       # tipos de dato y nulos por columna (sin print() alrededor)
```

### Selección y filtros
```python
tabla[["nombre", "monto_compra"]]              # varias columnas (doble corchete)
tabla[tabla["monto_compra"] > 50000]            # filtrar filas
tabla[tabla["sucursal"] == "Providencia"]       # filtrar por texto exacto

# Combinar condiciones en pandas: usar & (y) y | (o) -- NUNCA and/or
tabla[(tabla["monto"] > 50000) & (tabla["sucursal"] == "Providencia")]
```

### Columnas calculadas
```python
tabla["descuento"] = (tabla["monto_compra"] * 0.9).round(0)
tabla["categoria"] = tabla["monto_compra"].apply(clasificar_cliente)
# .apply() recibe la función SIN paréntesis -- se la "entregas", no la ejecutas tú.
```

### Agrupaciones
```python
tabla.groupby("sucursal")["monto_compra"].sum()     # total por sucursal
tabla.groupby("sucursal")["nombre"].count()          # cantidad de clientes
# El resultado es una Series (no DataFrame), ordenada alfabéticamente por defecto.
```

### Fechas
```python
tabla["fecha"] = pd.to_datetime(tabla["fecha"])            # texto -> fecha real
hoy = pd.Timestamp.today()
tabla["dias"] = (hoy - tabla["fecha"]).dt.days               # diferencia en días

# Filtrar por rango de fechas (paréntesis obligatorios en cada condición)
tabla[(tabla["fecha"] >= "2026-01-01") & (tabla["fecha"] <= "2026-01-15")]
```

---

## 3. AUTOMATIZACIÓN

### Gráficos con matplotlib
```python
import matplotlib.pyplot as plt

ventas_por_sucursal.plot(kind="bar")   # también: "line", "pie"
plt.title("Ventas por Sucursal")
plt.xlabel("Sucursal")
plt.ylabel("Monto ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico.png")   # SIEMPRE antes de plt.show()
plt.close()                  # cierra la figura (evita mezclar gráficos)
# En automatización sin supervisión: NUNCA usar plt.show() (pausa el script).
```

### Enviar correos con adjuntos
```python
from dotenv import load_dotenv
import os, smtplib
from email.message import EmailMessage

load_dotenv()   # carga variables desde el archivo .env (credenciales seguras)
remitente = os.getenv("EMAIL_REMITENTE")
password = os.getenv("EMAIL_PASSWORD")

mensaje = EmailMessage()
mensaje["Subject"] = "Asunto"
mensaje["From"] = remitente
mensaje["To"] = "destino@correo.com"
mensaje.set_content("Cuerpo del mensaje")

with open("reporte.xlsx", "rb") as archivo:
    mensaje.add_attachment(
        archivo.read(),
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="reporte.xlsx"
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(remitente, password)
    servidor.send_message(mensaje)

# IMPORTANTE: el archivo .env NUNCA se sube a GitHub (ver sección Git, .gitignore).
# Usar contraseña de aplicación de Gmail, no la contraseña normal de la cuenta.
```

### SQL básico con sqlite3
```python
import sqlite3

conexion = sqlite3.connect("basededatos.db")
tabla.to_sql("clientes", conexion, if_exists="replace", index=False)
conexion.close()

conexion = sqlite3.connect("basededatos.db")
resultado = pd.read_sql("SELECT * FROM clientes WHERE monto_compra > 50000", conexion)
conexion.close()
```

---

## 4. LIMPIEZA DE DATOS REALES

### Diagnóstico (medir el problema antes de arreglarlo)
```python
tabla.isnull().sum()               # cantidad de nulos por columna
tabla.duplicated().sum()           # cantidad de filas duplicadas exactas
tabla.duplicated(keep=False)       # marca TODAS las apariciones de duplicados (no solo la copia)
tabla["columna"].unique()          # valores distintos en una columna
tabla["columna"].value_counts()    # cuenta cuántas veces aparece cada valor

# OJO: sin un id_cliente único, ".duplicated()" puede confundir coincidencias
# de azar con duplicados reales. Un ID único elimina esa ambigüedad.
```

### Limpieza
```python
tabla = tabla.drop_duplicates()                       # elimina copias exactas
tabla["sucursal"] = tabla["sucursal"].str.strip()      # quita espacios extra
tabla["sucursal"] = tabla["sucursal"].str.title()      # formato "Palabra Palabra"
tabla["sucursal"] = tabla["sucursal"].replace("Maipu", "Maipú")  # corrige contenido
# .strip() y .title() arreglan FORMATO, no CONTENIDO (no agregan tildes faltantes).

tabla = tabla.dropna(subset=["monto_compra"])   # elimina filas con nulo en esa columna
# Regla de criterio de negocio: NUNCA rellenar con 0 un dato que "no se sabe"
# (0 significa "compró cero", no "no sé cuánto compró") -- especialmente si
# se van a calcular promedios, no solo sumas.
```

---

## 5. MANEJO DE ERRORES (try/except)

```python
try:
    tabla = pd.read_excel("archivo.xlsx")
    tabla["columna_que_puede_no_existir"]

except FileNotFoundError as error:
    print(f"No se encontró el archivo: {error}")

except KeyError as error:
    print(f"Falta una columna esperada: {error}")

except Exception as error:
    print(f"Error inesperado: {error}")

# REGLA DE ORO: errores específicos PRIMERO, Exception (genérico) AL FINAL.
# Python revisa los except de arriba hacia abajo y se detiene en el primero
# que coincide -- si Exception fuera primero, los demás nunca se alcanzarían.
# "as error" guarda el detalle técnico para poder mostrarlo o loguearlo.
```

---

## 6. PROGRAMACIÓN DE TAREAS (schedule)

```python
import schedule
import time

def tarea():
    print("Se ejecutó")

schedule.every(5).seconds.do(tarea)          # cada 5 segundos
schedule.every().day.at("09:00").do(tarea)   # todos los días a las 09:00

while True:
    schedule.run_pending()   # revisa si ya toca ejecutar algo
    time.sleep(1)            # pausa 1 seg (evita consumir CPU sin necesidad)
# Se detiene manualmente con Ctrl + C (genera KeyboardInterrupt, no es un error real)

# Para reutilizar un script como función importable (principio DRY):
# archivo A: envolver todo el código dentro de "def ejecutar_algo():"
# archivo B: from archivo_a import ejecutar_algo
# En un entorno de trabajo real, esto se reemplaza por el Programador de
# Tareas de Windows o un servidor -- no se deja una terminal abierta 24/7.
```

---

## 7. JUPYTER NOTEBOOK

- Archivo `.ipynb`, se ejecuta **celda por celda** (`Shift + Enter`), no todo de una vez.
- Las variables quedan "vivas" en memoria entre celdas -- riesgo: ejecutar celdas
  fuera de orden puede dar resultados inconsistentes con lo que se ve en pantalla.
- **Antes de compartir un notebook**: usar "Restart" + "Ejecutar todo" para garantizar
  que es reproducible de arriba hacia abajo, sin depender del historial de ejecuciones.
- Dejar un DataFrame como última línea de una celda (sin `print()`) lo muestra
  automáticamente con formato de tabla.

---

## 8. PROGRAMACIÓN ORIENTADA A OBJETOS (POO)

### Clases
```python
class Cliente:
    def __init__(self, nombre, monto_compra, sucursal):
        self.nombre = nombre
        self.monto_compra = monto_compra
        self.sucursal = sucursal

    def clasificar(self):
        if self.monto_compra >= 90000:
            return "VIP"
        elif self.monto_compra >= 50000:
            return "Premium"
        else:
            return "Regular"

cliente_1 = Cliente("María", 45990, "Providencia")
cliente_1.nombre           # acceso a atributo (sin corchetes, con punto)
cliente_1.clasificar()     # llamar a un método (usa self.monto_compra internamente)

# self = "este objeto específico". Python lo pasa automáticamente,
# nunca se escribe manualmente al crear o llamar al objeto.
# __init__ = constructor, se ejecuta automáticamente al crear el objeto.
```

### Herencia
```python
class ClienteVIP(Cliente):
    def __init__(self, nombre, monto_compra, sucursal, ejecutivo):
        super().__init__(nombre, monto_compra, sucursal)  # reutiliza el padre
        self.ejecutivo = ejecutivo

    def calcular_descuento(self):    # sobrescribe (override) el comportamiento
        return round(self.monto_compra * 0.85)

# ClienteVIP hereda TODO de Cliente (incluido .clasificar(), sin reescribirlo).
# super().__init__() evita duplicar código -- principio DRY aplicado a POO.
```

### Conectar objetos con pandas
```python
datos = []
for cliente in lista_de_clientes:
    datos.append({
        "nombre": cliente.nombre,
        "categoria": cliente.clasificar()   # se llama al método al armar el dict
    })
tabla = pd.DataFrame(datos)
# pandas no sabe leer objetos propios directamente -- el diccionario es el "puente".
```

---

## 9. PANDAS AVANZADO

### merge() — cruzar tablas (equivalente a JOIN en SQL)
```python
tabla_completa = clientes.merge(sucursales_info, on="sucursal")
# Cruza por la columna "sucursal", presente en ambas tablas.
# PELIGRO: por defecto es un INNER JOIN -- si el texto de cruce no coincide
# EXACTAMENTE (ej. "Maipú" vs "Maipu"), la fila completa desaparece SIN AVISO.
# Siempre limpiar (.str.strip().str.title()) las columnas de cruce ANTES de merge().
```

### pivot_table() — tabla dinámica (igual que en Excel)
```python
pd.pivot_table(
    tabla,
    values="monto_compra",     # qué se agrega (el "Valores" de Excel)
    index="sucursal",          # filas
    columns="categoria",       # columnas
    aggfunc="sum",              # suma, count, mean...
    fill_value=0                # reemplaza NaN por 0 si no hay datos
)
```

---

## 10. GIT Y GITHUB

*(Ver también el apunte separado `apuntes_git.md` para el detalle completo comentado)*

```bash
git init                                  # crear repositorio nuevo
git clone <url>                           # descargar uno que ya existe
git status                                # ver qué cambió
git add .                                 # preparar todos los cambios
git commit -m "mensaje"                   # guardar un punto en el historial
git push                                  # subir a GitHub
git remote add origin <url>               # conectar con GitHub (primera vez)
git remote set-url origin <url>           # cambiar la URL remota

# .gitignore: SIEMPRE antes del primer "add", nunca después.
# Contiene: .env, __pycache__/, *.pyc -- protege credenciales del historial.
# GitHub NO ejecuta código -- solo lo guarda y lo muestra (para eso está git clone).
```

---

## 11. PROYECTO FINANCIERO: NUMPY + YFINANCE

```python
import yfinance as yf
import numpy as np

precios = yf.download(["AAPL", "MSFT"], start="2024-01-01", end="2025-01-01")["Close"]

retornos = precios.pct_change()                     # retorno diario (% de cambio)
volatilidad_anual = retornos.std() * np.sqrt(252)   # riesgo anualizado (252 días hábiles)
retorno_total = (precios.iloc[-1] / precios.iloc[0]) - 1   # retorno del período completo

correlacion = retornos.corr()   # -1 a 1: qué tan juntos se mueven dos activos
# Correlación alta = poca diversificación (bueno saberlo para armar portafolios)

# Riesgo de un portafolio combinado (no es solo el promedio de riesgos individuales):
pesos = np.array([0.5, 0.5])
matriz_covarianza = retornos.cov() * 252
varianza_portafolio = np.dot(pesos.T, np.dot(matriz_covarianza, pesos))
volatilidad_portafolio = np.sqrt(varianza_portafolio)
# Hallazgo clave: combinar activos con correlación < 1 reduce el riesgo total
# por debajo del riesgo de cualquier activo individual (efecto diversificación).

# Normalizar precios para graficar comparación de desempeño real:
precios_normalizados = precios / precios.iloc[0]   # todos parten en 1.0
```

---

## 12. SQL SERVER REAL (pyodbc)

```python
import pyodbc

conexion = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"     # doble \\ porque \ es caracter especial en Python
    "DATABASE=NombreBaseDeDatos;"
    "Trusted_Connection=yes;"            # usa autenticación de Windows
)
tabla = pd.read_sql("SELECT * FROM clientes", conexion)
conexion.close()

pyodbc.drivers()   # lista los drivers ODBC instalados en el sistema (para diagnosticar)

# pd.read_sql() funciona EXACTAMENTE IGUAL sin importar si la conexión es
# sqlite3, SQL Server, o cualquier otra -- solo cambia cómo te conectas.
```

---

## 13. APIS EXTERNAS (requests)

```python
import requests

respuesta = requests.get("https://mindicador.cl/api")
datos = respuesta.json()          # convierte la respuesta (JSON) en diccionario Python

datos["dolar"]              # diccionario interno del indicador
datos["dolar"]["valor"]     # acceso encadenado -- JSON anidado = diccionarios anidados

# JSON y diccionarios de Python son prácticamente lo mismo estructuralmente.
# GitHub, APIs, casi todo en internet habla en formato JSON.
```

---

## 14. RENDIMIENTO CON DATOS MASIVOS

```python
import time

# MAL (lento): acceder fila por fila dentro de un for
inicio = time.time()
for i in range(len(tabla)):
    valor = tabla.iloc[i]["monto_compra"]   # "overhead" repetido 500.000 veces
fin = time.time()

# MEJOR: .apply() sobre toda la columna de una vez
tabla["monto_compra"].apply(clasificar_cliente)

# MEJOR AÚN: vectorización pura, sin llamar a ninguna función fila por fila
np.select(
    [tabla["monto"] >= 90000, tabla["monto"] >= 50000],
    ["VIP", "Premium"],
    default="Regular"
)

# Resultados reales medidos (500.000 filas):
# loop manual (.iloc)  -> ~25 segundos
# .apply()             -> ~0.15 segundos   (~168x más rápido)
# np.select()          -> ~0.02 segundos   (~1.000x más rápido que el loop)

# Con datos MUY grandes (varios cientos de miles / millones de filas), además:
# - Filtrar en SQL (WHERE) antes de traer datos a pandas, no traer todo y filtrar después.
# - Usar tipos de dato "category" para columnas de texto muy repetitivo (ahorra memoria).
# - chunksize en read_csv/read_sql para procesar por partes sin cargar todo en RAM.
# - Herramientas como Polars o Spark/Databricks entran en juego a escala de "big data" real.
```

---

## RESUMEN DE PRINCIPIOS TRANSVERSALES (aplican a todo lo anterior)

- **DRY** (Don't Repeat Yourself): si copias el mismo código en dos lugares, conviértelo
  en función o clase reutilizable -- evita tener que recordar actualizar ambas copias.
- **Nunca hardcodear credenciales**: usar `.env` + `.gitignore`, nunca escribir
  contraseñas directamente en el código.
- **Nunca confiar ciegamente en que dos textos "se ven iguales"**: siempre limpiar
  (`.str.strip()`, `.str.title()`) antes de comparar, agrupar, o cruzar datos.
- **No reportar una conclusión que los datos no puedan sostener**: sin un identificador
  único, "duplicados" puede ser solo coincidencia -- comunicar la limitación, no adivinar.
- **Reproducibilidad**: fijar semillas (`np.random.seed()`), reiniciar notebooks antes
  de compartirlos, escribir mensajes de commit claros -- todo para que el trabajo sea
  verificable por otra persona (o por ti mismo, en el futuro).
