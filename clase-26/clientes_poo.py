import pandas as pd


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

    def calcular_descuento(self):
        return round(self.monto_compra * 0.9)


lista_clientes = [
    Cliente("María Fernanda Rojas", 45990, "Sucursal Providencia"),
    Cliente("Javier Pérez Silva", 33990, "Sucursal Las Condes"),
    Cliente("Ana Torres", 78500, "Sucursal Concepción"),
    Cliente("Carlos Ossandón", 100500, "Sucursal Maipú"),
]

datos_para_tabla = []

for cliente in lista_clientes:
    datos_para_tabla.append({
        "nombre": cliente.nombre,
        "monto_compra": cliente.monto_compra,
        "sucursal": cliente.sucursal,
        "categoria": cliente.clasificar(),
        "monto_con_descuento": cliente.calcular_descuento()
    })

tabla = pd.DataFrame(datos_para_tabla)
print(tabla)



