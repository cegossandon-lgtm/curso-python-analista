from cierre_mensual import ejecutar_cierre_mensual
import schedule
import time

schedule.every().day.at("05:18").do(ejecutar_cierre_mensual)

print("Programador de tareas iniciado. Esperando la hora programada...")

while True:
    schedule.run_pending()
    time.sleep(1)

