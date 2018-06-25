from ..Rational import Rational
from ..QuadIrrational import QuadIrrational

def test_addition():
    a = Rational(1,2)
    b = Rational(1,3)
    c = Rational(5,6)
    A = QuadIrrational(a, b, 3)
    B = QuadIrrational(b, a, 3)
    C = QuadIrrational(c, c, 3)
    D = QuadIrrational(1, 1, 2)
    assert A + B == C
    assert 1 + D == QuadIrrational(2,1,2)

def test_subtraction():
    a = Rational(1,2)
    b = Rational(1,3)
    c = Rational(1,6)
    A = QuadIrrational(a, b, 3)
    B = QuadIrrational(b, a, 3)
    C = QuadIrrational(c, -c, 3)
    D = QuadIrrational(1, 1, 2)
    assert A - B == C
    assert 1 - D == QuadIrrational(0,-1,2)

