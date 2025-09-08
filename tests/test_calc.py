from app.calc import soma, multiplicacao, divisao, subtracao

def test_soma():
    assert soma(2, 3) == 5

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

def test_subtracao():
    assert subtracao(5, 3) == 2

