try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError as error:
    print(f"Error: no se puede dividir por cero. Detalle: {error}")
