from app.calc import soma, multiplica

def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_subtrai():
    assert subtrai(5, 3) == 2

def test_divisao():
    assert divide(6, 3) == 2

