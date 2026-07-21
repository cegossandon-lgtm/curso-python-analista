import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


load_dotenv()

tabla_clientes = pd.read_excel("clase-07/clientes_comercial_andes.xlsx")

def clasificar_cliente(monto):
    if monto >= 90000:
        return "VIP"
    elif monto >= 50000:
        return "Premium"
    else:
        return "Regular"

tabla_clientes["categoria"] = tabla_clientes["monto_compra"].apply(clasificar_cliente)

tabla_clientes["monto_con_descuento"] = (tabla_clientes["monto_compra"] * 0.9).round(0)
tabla_clientes["impuesto_19"] = (tabla_clientes["monto_compra"] * 0.19).round(0)


ventas_por_sucursal = tabla_clientes.groupby("sucursal")["monto_compra"].sum()

ventas_por_sucursal.plot(kind="bar")
plt.title("Ventas Totales por Sucursal - Cierre Mensual")
plt.xlabel("Sucursal")
plt.ylabel("Monto Total ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("clase-18/grafico_cierre_mensual.png")
plt.close()

tabla_clientes.to_excel("clase-18/reporte_cierre_mensual.xlsx", index=False)

remitente = os.getenv("EMAIL_REMITENTE")
password = os.getenv("EMAIL_PASSWORD")

total_ventas = tabla_clientes["monto_compra"].sum()
cantidad_clientes = len(tabla_clientes)

mensaje = EmailMessage()
mensaje["Subject"] = "Cierre Mensual - Comercial Andes S.A."
mensaje["From"] = remitente
mensaje["To"] = "cegossandon@gmail.com"
mensaje.set_content(
    f"Resumen del cierre mensual:\n\nTotal de ventas: ${total_ventas}\nCantidad de clientes: {cantidad_clientes}\n\nSe adjunta el reporte completo en Excel y el gráfico de ventas por sucursal."
)

with open("clase-18/reporte_cierre_mensual.xlsx", "rb") as archivo_excel:
    mensaje.add_attachment(
        archivo_excel.read(),
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="reporte_cierre_mensual.xlsx"
    )

with open("clase-18/grafico_cierre_mensual.png", "rb") as archivo_grafico:
    mensaje.add_attachment(
        archivo_grafico.read(),
        maintype="image",
        subtype="png",
        filename="grafico_cierre_mensual.png"
    )


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(remitente, password)
    servidor.send_message(mensaje)

print("Cierre mensual enviado correctamente.")

