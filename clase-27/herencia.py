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


class ClienteVIP(Cliente):
    def __init__(self, nombre, monto_compra, sucursal, ejecutivo_asignado):
        super().__init__(nombre, monto_compra, sucursal)
        self.ejecutivo_asignado = ejecutivo_asignado

    def calcular_descuento(self):
        return round(self.monto_compra * 0.85)


cliente_vip_1 = ClienteVIP("Carlos Ossandón", 100500, "Sucursal Maipú", "Fernanda Muñoz")

print(cliente_vip_1.nombre)
print(cliente_vip_1.ejecutivo_asignado)
print(cliente_vip_1.clasificar())
print(cliente_vip_1.calcular_descuento())

cliente_normal = Cliente("Cliente de Prueba", 100500, "Sucursal Providencia")
cliente_vip_2 = ClienteVIP("Cliente VIP de Prueba", 100500, "Sucursal Providencia", "Fernanda Muñoz")

print(f"Descuento normal: {cliente_normal.calcular_descuento()}")
print(f"Descuento VIP: {cliente_vip_2.calcular_descuento()}")

