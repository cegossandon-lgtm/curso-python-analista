import schedule
import time

def tarea_de_prueba():
    print("¡La tarea se ejecutó!")

schedule.every(5).seconds.do(tarea_de_prueba)

while True:
    schedule.run_pending()
    time.sleep(1)

