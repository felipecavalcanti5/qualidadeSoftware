from modulo import calcula_desconto 

def test_calcula_desconto():
    # Testes com preço e percentual
    assert calcula_desconto(100, 20) == 80  # 20% de desconto em 100
    assert calcula_desconto(200, 50) == 100  # 50% de desconto em 200
    assert calcula_desconto(150, 10) == 135  # 10% de desconto em 150
    assert calcula_desconto(80, 25) == 60    # 25% de desconto em 80
    assert calcula_desconto(1000, 5) == 950  # 5% de desconto em 1000
    assert calcula_desconto(0, 50) == 0      # 50% de desconto em 0
    assert calcula_desconto(100, 0) == 100    # 0% de desconto em 100
