from sum import soma

def test_soma_numeros_positivos():
    assert soma(2, 3) == 5

def test_soma_numeros_negativos():
    assert soma(-4, -6) == -10

def test_soma_zero():
    assert soma(0, 5) == 5
