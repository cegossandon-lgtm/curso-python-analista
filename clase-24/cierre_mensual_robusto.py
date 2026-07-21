import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()


def enviar_correo(asunto, cuerpo, archivos_adjuntos=None):
    remitente = os.getenv("EMAIL_REMITENTE")
    password = os.getenv("EMAIL_PASSWORD")

    mensaje = EmailMessage()
    mensaje["Subject"] = asunto
    mensaje["From"] = remitente
    mensaje["To"] = "cegossandon@gmail.com"
    mensaje.set_content(cuerpo)

    if archivos_adjuntos:
        for ruta_archivo in archivos_adjuntos:
            with open(ruta_archivo, "rb") as archivo:
                nombre_archivo = os.path.basename(ruta_archivo)
                if nombre_archivo.endswith(".xlsx"):
                    mensaje.add_attachment(
                        archivo.read(),
                        maintype="application",
                        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        filename=nombre_archivo,
                    )
                elif nombre_archivo.endswith(".png"):
                    mensaje.add_attachment(
                        archivo.read(),
                        maintype="image",
                        subtype="png",
                        filename=nombre_archivo,
                    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remitente, password)
        servidor.send_message(mensaje)


try:
    tabla = pd.read_excel("clase-20/clientes_sucios.xlsx")

    tabla = tabla.drop_duplicates()

    tabla["sucursal"] = tabla["sucursal"].str.strip()
    tabla["sucursal"] = tabla["sucursal"].str.title()
    tabla["sucursal"] = tabla["sucursal"].replace("Sucursal Maipu", "Sucursal Maipú")

    tabla = tabla.dropna(subset=["monto_compra"])

    def clasificar_cliente(monto):
        if monto >= 90000:
            return "VIP"
        elif monto >= 50000:
            return "Premium"
        else:
            return "Regular"

    tabla["categoria"] = tabla["monto_compra"].apply(clasificar_cliente)

    ventas_por_sucursal = tabla.groupby("sucursal")["monto_compra"].sum()

    ventas_por_sucursal.plot(kind="bar")
    plt.title("Ventas Totales por Sucursal - Cierre Mensual")
    plt.xlabel("Sucursal")
    plt.ylabel("Monto Total ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("clase-24/grafico_cierre_mensual.png")
    plt.close()

    tabla.to_excel("clase-24/reporte_cierre_mensual.xlsx", index=False)

    total_ventas = tabla["monto_compra"].sum()
    cantidad_clientes = len(tabla)

    enviar_correo(
        asunto="Cierre Mensual - Comercial Andes S.A.",
        cuerpo=(
            f"Resumen del cierre mensual:\n\n"
            f"Total de ventas: ${total_ventas}\n"
            f"Cantidad de clientes: {cantidad_clientes}\n\n"
            f"Se adjunta el reporte completo y el gráfico."
        ),
        archivos_adjuntos=[
            "clase-24/reporte_cierre_mensual.xlsx",
            "clase-24/grafico_cierre_mensual.png",
        ],
    )

    print("Cierre mensual procesado y enviado correctamente.")

except Exception as error:
    enviar_correo(
        asunto="ERROR - Cierre Mensual no se pudo generar",
        cuerpo=f"El proceso de cierre mensual falló.\n\nDetalle técnico: {error}",
    )
    print(f"Error manejado y notificado por correo: {error}")

