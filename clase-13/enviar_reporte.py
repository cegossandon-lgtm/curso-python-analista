from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage
import pandas as pd

load_dotenv()
remitente = os.getenv("EMAIL_REMITENTE")
password = os.getenv("EMAIL_PASSWORD")

cliente_1 = {"nombre": "María Fernanda Rojas", "monto_compra": 45990, "sucursal": "Sucursal Providencia"}
cliente_2 = {"nombre": "Javier Pérez Silva", "monto_compra": 33990, "sucursal": "Sucursal Las Condes"}
cliente_3 = {"nombre": "Ana Torres", "monto_compra": 78500, "sucursal": "Sucursal Concepción"}
cliente_4 = {"nombre": "Carlos Ossandón", "monto_compra": 100500, "sucursal": "Sucursal Maipú"}

clientes = [cliente_1, cliente_2, cliente_3, cliente_4]
tabla_clientes = pd.DataFrame(clientes)

tabla_clientes.to_excel("clase-13/reporte_clientes.xlsx", index=False)

mensaje = EmailMessage()

mensaje["Subject"] = "Reporte de Clientes - Comercial Andes S.A."
mensaje["From"] = remitente
mensaje["To"] = "cegossandon@gmail.com"
mensaje.set_content("Adjunto el reporte de clientes de Comercial Andes S.A. Saludos.")

with open("clase-13/reporte_clientes.xlsx", "rb") as archivo:
    contenido_archivo = archivo.read()

mensaje.add_attachment(
    contenido_archivo,
    maintype="application",
    subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    filename="reporte_clientes.xlsx"
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(remitente, password)
    servidor.send_message(mensaje)

