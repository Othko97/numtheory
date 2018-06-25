"""Periodic Simple Continued Fractions"""

#Imports
from .QuadIrrational import QuadIrrational
from .Rational import Rational

#Class Definition
class PeriodicContFrac():
    def __init__(self, quadIrrational):
        """Returns periodic simple continued fraction representation"""
        self.quadirrat = quadIrrational
        self.rep = []
        previters = []
        nextiter = quadIrrational

        while nextiter not in previters:
            previters.append(nextiter)
            floor = int(abs(nextiter))
            self.rep.append(floor)
            nextiter = (nextiter - floor)**-1
        
        self.initblock = previters.index(nextiter)

    
    def __repr__(self):
        """Nice output"""
        return "[{head};{initblock};{tail}]".format(head = self.rep[0], initblock = ",".join(map(str, self.rep[1:self.initblock + 1])) ,tail = ",".join(map(str, self.rep[self.initblock+2:])))

    def __str__(self):
        """Nice output"""
        return "[{head};{initblock};{tail}]".format(head = self.rep[0], initblock = ",".join(map(str, self.rep[1:self.initblock + 1])) ,tail = ",".join(map(str, self.rep[self.initblock+2:])))


    def frac(self):
        """Returns Quadratic Irrational Associated with Continued Fraction"""
        return self.quadirrat
    
    def __abs__(self):
        """Float value"""
        return abs(self.frac())
    
    def __add__(self, other):
        """Addition"""
        if isinstance(other, PeriodicContFrac):
            return PeriodicContFrac(self.frac() + other.frac())
        if isinstance(other, QuadIrrational) or isinstance(other, Rational) or isinstance(other, int):
            return PeriodicContFrac(self.frac() + other)
    
    __radd__ = __add__

    def __sub__(self, other):
        """Subtraction"""
        if isinstance(other, PeriodicContFrac):
            return PeriodicContFrac(self.frac() - other.frac())
        if isinstance(other, QuadIrrational) or isinstance(other, Rational) or isinstance(other, int):
            return PeriodicContFrac(self.frac() - other)
    
    def __neg__(self):
        """Allow negation"""
        return 0 - self

    def __rsub__(self, other):
        """Make subtraction anti-commutative"""
        if isinstance(other, QuadIrrational) or isinstance(other, Rational) or isinstance(other, int):
            return PeriodicContFrac(other - self.frac())

    def __mul__(self, other):
        """Multiplication"""
        if isinstance(other, PeriodicContFrac):
            return PeriodicContFrac(self.frac() * other.frac())
        if isinstance(other, QuadIrrational) or isinstance(other, Rational) or isinstance(other, int):
            return PeriodicContFrac(self.frac() * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        """Division"""
        if isinstance(other, PeriodicContFrac):
            return PeriodicContFrac(self.frac() / other.frac())
        if isinstance(other, QuadIrrational) or isinstance(other, Rational) or isinstance(other, int):
            return PeriodicContFrac(self.frac() / other)
    
    def __rtruediv__(self, other):
        """Make division nice"""
        if isinstance(other, QuadIrrational) or isinstance(other, Rational) or isinstance(other, int):
            return PeriodicContFrac(other / self.frac())
    
    def __pow__(self, other):
        """Exponentiation"""
        if isinstance(other, int):
            return PeriodicContFrac(self.frac() ** other)
        
    def recip(self):
        """Reciprocal"""
        return self ** -1
    
    def __eq__(self, other):
        """Equality of SCFs"""
        if isinstance(other, PeriodicContFrac):
            return self.frac() == other.frac()
        if isinstance(other, QuadIrrational) or isinstance(other, Rational) or isinstance(other, int):
            return self.frac() == other