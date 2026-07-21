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


cliente_1 = Cliente("María Fernanda Rojas", 45990, "Sucursal Providencia")
cliente_2 = Cliente("Javier Pérez Silva", 33990, "Sucursal Las Condes")

print(cliente_1.nombre)
print(cliente_1.monto_compra)
print(cliente_2.sucursal)

print(cliente_1.clasificar())
print(cliente_2.clasificar())

print(cliente_1.calcular_descuento())
