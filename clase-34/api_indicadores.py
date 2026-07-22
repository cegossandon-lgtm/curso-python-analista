import requests
import pandas as pd

respuesta = requests.get("https://mindicador.cl/api")
datos = respuesta.json()

print(datos.keys())

print(datos["dolar"])
print(datos["dolar"]["valor"])


indicadores_de_interes = ["dolar", "euro", "uf", "utm", "ipc"]

lista_indicadores = []

for indicador in indicadores_de_interes:
    lista_indicadores.append({
        "indicador": datos[indicador]["nombre"],
        "valor": datos[indicador]["valor"],
        "unidad": datos[indicador]["unidad_medida"],
        "fecha": datos[indicador]["fecha"]
    })

tabla_indicadores = pd.DataFrame(lista_indicadores)
print(tabla_indicadores)


tabla_indicadores.to_excel("clase-34/indicadores_economicos.xlsx", index=False)
print("Indicadores exportados correctamente.")



