import pandas as pd

pagos = pd.read_csv("clase-14/pagos_banco.csv")

pagos["fecha_pago"] = pd.to_datetime(pagos["fecha_pago"])

pagos.info()

hoy = pd.Timestamp.today()
pagos["dias_transcurridos"] = (hoy - pagos["fecha_pago"]).dt.days

print(pagos)

primera_quincena = pagos[(pagos["fecha_pago"] >= "2026-07-01") & (pagos["fecha_pago"] <= "2026-07-15")]

print(primera_quincena)
