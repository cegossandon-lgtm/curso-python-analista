import pandas as pd
import random

nombres = ["María", "Javier", "Ana", "Carlos", "Pedro", "Sofía", "Diego", "Valentina", "Andrés", "Camila"]
apellidos = ["Rojas", "Pérez", "Torres", "Ossandón", "González", "Muñoz", "Silva", "Contreras", "Flores", "Vidal"]
sucursales = ["Sucursal Providencia", "Sucursal Las Condes", "sucursal Concepción", "SUCURSAL MAIPU", "Sucursal Providencia "]


clientes = []

for i in range(5000):
    id_cliente = i + 1
    nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"
    monto = random.choice([random.randint(10000, 150000), None])
    sucursal = random.choice(sucursales)

    cliente = {
        "id_cliente": id_cliente,
        "nombre": nombre_completo,
        "monto_compra": monto,
        "sucursal": sucursal
    }
    clientes.append(cliente)


duplicados = random.sample(clientes, 300)
clientes = clientes + duplicados

tabla_clientes_sucia = pd.DataFrame(clientes)
tabla_clientes_sucia.to_excel("clase-20/clientes_sucios.xlsx", index=False)

print(f"Archivo generado con {len(tabla_clientes_sucia)} filas.")

