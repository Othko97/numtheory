from ..Rational import Rational

def test_addition():
    a = Rational(1,2)
    b = Rational(1,3)
    assert a + b == Rational(5,6)
    assert a + 1 == Rational(3,2)
    assert a + b == b + a
    assert a + 1 == 1 + a

def test_subtraction():
    a = Rational(1,2)
    b = Rational(1,3)
    assert a - b == Rational(1,6)
    assert a - 1 == Rational(-1,2)
    assert a - b == -(b - a)
    assert a - 1 == -(1 - a)

def test_multiplication():
    a = Rational(1,2)
    b = Rational(1,3)
    assert a * b == Rational(1,6)
    assert a * 2 == 1
    assert a * b == b * a
    assert a * 2 == 2 * a

def test_division():
    a = Rational(1,2)
    b = Rational(1,3)
    assert a / b == Rational(3,2)
    assert a / 2 == Rational(1,4)
    assert a / b == 1 / (b / a)
    assert a / 2 == 1 / (2 / a)

def test_exponentiation():
    a = Rational(1,2)
    assert a ** 2 == Rational(1,4)
    assert a ** -2 == 4
    assert a ** 0 == 1