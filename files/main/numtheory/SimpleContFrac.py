"""Class for simple continued fraction representation of a number"""

from .Rational import Rational

#Extended Euclidean Algorithm to get continued fractions
def exeuclid(a, b):
	"""returns gcd of a, b and list of quotients to get there"""
	#set n, m consistently
	n = max(a,b)
	m = min(a,b)
	
	quotients = []
	
	#follow euclidean algorithm
	while m != 0:
		quotients.append(n//m)
		t = m
		m = n % t
		n = t
	
	return (n, quotients)

class SimpleContFrac():
    def __init__(self, rtnl):
        """Returns finite simple continued fraction representation of a given rational"""
        self.values = []
        if rtnl.a < rtnl.b:
            self.values.append(0)
        self.values += exeuclid(rtnl.a, rtnl.b)[1]
    
    def __repr__(self):
        return "[{head};{tail}]".format(head = self.values[0], tail = ",".join(map(str, self.values[1:])))
    
    def __str__(self):
        return "[{head};{tail}]".format(head = self.values[0], tail = ",".join(map(str, self.values[1:])))

    def frac(self):
        """Returns Rational value of the finite continued fraction"""
        p0 = 0
        p1 = 1
        q0 = 1
        q1 = 0

        for i in self.values:
            p = p1*i + p0
            q = q1*i + q0

            p0 = p1
            p1 = p
            q0 = q1
            q1 = q
        
        return Rational(p, q)
    
    def __abs__(self):
        """Float value"""
        return abs(self.frac())
    
    def __add__(self, other):
        """Addition"""
        if isinstance(other, SimpleContFrac):
            return SimpleContFrac(self.frac() + other.frac())
        if isinstance(other, Rational) or isinstance(other, int):
            return SimpleContFrac(self.frac() + other)
    
    __radd__ = __add__

    def __sub__(self, other):
        """Subtraction"""
        if isinstance(other, SimpleContFrac):
            return SimpleContFrac(self.frac() - other.frac())
        if isinstance(other, Rational) or isinstance(other, int):
            return SimpleContFrac(self.frac() - other)
    
    def __neg__(self):
        """Allow negation"""
        return 0 - self

    def __rsub__(self, other):
        """Make subtraction anti-commutative"""
        if isinstance(other, Rational) or isinstance(other, int):
            return SimpleContFrac(other - self.frac())

    def __mul__(self, other):
        """Multiplication"""
        if isinstance(other, SimpleContFrac):
            return SimpleContFrac(self.frac() * other.frac())
        if isinstance(other, Rational) or isinstance(other, int):
            return SimpleContFrac(self.frac() * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        """Division"""
        if isinstance(other, SimpleContFrac):
            return SimpleContFrac(self.frac() / other.frac())
        if isinstance(other, Rational) or isinstance(other, int):
            return SimpleContFrac(self.frac() / other)
    
    def __rtruediv__(self, other):
        """Make division nice"""
        if isinstance(other, Rational) or isinstance(other, int):
            return SimpleContFrac(other / self.frac())
    
    def __pow__(self, other):
        """Exponentiation"""
        if isinstance(other, int):
            return SimpleContFrac(self.frac() ** other)
        
    def recip(self):
        """Reciprocal"""
        return self ** -1
    
    def __eq__(self, other):
        """Equality of SCFs"""
        if isinstance(other, SimpleContFrac):
            return self.frac() == other.frac()
        if isinstance(other, Rational) or isinstance(other, int):
            return self.frac() == other