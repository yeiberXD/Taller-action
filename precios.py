def calcular_precio(precio_base, cantidad, descuento=0):
    total = precio_base * cantidad
    return total + (total * descuento / 100)
