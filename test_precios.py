from precios import calcular_precio

def test_sin_descuento():
    assert calcular_precio(100, 2) == 200

def test_con_descuento():
    assert calcular_precio(100, 2, 10) == 180
