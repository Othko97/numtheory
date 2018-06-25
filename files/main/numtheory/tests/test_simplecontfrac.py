from ..SimpleContFrac import SimpleContFrac
from ..Rational import Rational

def test_representation():
    a = Rational(5,8)
    assert str(SimpleContFrac(a)) == '[0;1,1,1,2]'

def test_addition():
    a = Rational(5,8)
    b = Rational(8,13)
    assert SimpleContFrac(a) + SimpleContFrac(Rational(-1,104)) == SimpleContFrac(b)

def test_subtraction():
    a = Rational(1,2)
    b = Rational(1,3)
    assert SimpleContFrac(a) - SimpleContFrac(b) == SimpleContFrac(Rational(1,6))

def test_multiplication():
    a = SimpleContFrac(Rational(1,2))
    b = SimpleContFrac(Rational(1,3))
    assert a * b == SimpleContFrac(Rational(1,6))

def test_divide():
    a = SimpleContFrac(Rational(2,1))
    b = SimpleContFrac(Rational(3,1))
    assert a / b == SimpleContFrac(Rational(2,3))

def test_neg():
    a = SimpleContFrac(Rational(1,2))
    assert -a == SimpleContFrac(Rational(-1,2))