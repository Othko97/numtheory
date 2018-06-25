# pylint: disable=unused-variable

"""Object to represent rational numbers"""

#Euclidean Algorithm to cancel down fraction
def euclid(a, b):
	"""returns gcd of a, b as found by Euclidean Algorithm"""
	#set n, m consistently
	n = max(a,b)
	m = min(a,b)
	
	#follow euclidean algorithm
	while m != 0:
		t = m			
		m = n % t
		n = t
	return n

#Class for Rational Number
class Rational():

	def __init__(self, a, b):
		"""Constructor, ensures non-zero denominator, reduced"""
		if b != 0:
			gcd = euclid(abs(a), abs(b))
			self.a = (a//gcd) * (b//abs(b))
			self.b = abs(b//gcd)
		else:
			print("denominator must be nonzero")
	
	def __repr__(self):
		"""Representation as a/b"""
		if self.b != 1:
			return "{self.a}/{self.b}".format(self=self)
		else:
			return str(self.a)

	def __eq__(self, other):
		"""Checks equality of Rationals (including with integers)"""
		if isinstance(other, Rational):
			if self.a * other.b == self.b * other.a:
				return True
			return False
		if isinstance(other, int):
			if self.a  == self.b * other:
				return True
			return False
		
		
	def __add__(self, other):
		"""Addition of rationals and integers (as rationals)"""
		if isinstance(other, Rational):
			return Rational(self.a*other.b + self.b* other.a, self.b*other.b)
		if isinstance(other, int):
			return self + Rational(other, 1)
	
	#Make addition commutative
	__radd__ = __add__
	
	def __sub__(self, other):
		"""Subtraction of rationals and integers (as rationals)"""
		if isinstance(other, Rational):
			return Rational(self.a*other.b - self.b*other.a, self.b*other.b)
		if isinstance(other, int):
			return self - Rational(other, 1)
			
	def __rsub__(self, other):
		"""Subtraction of Rationals from integers"""
		if isinstance(other, int):
			return Rational(other, 1) - self
	
	def __neg__(self):
		return -1 * self
	
		
	def __mul__(self, other):
		"""Multiplication of rationals and integers (as rationals)"""
		if isinstance(other, Rational):
			return Rational(self.a*other.a, self.b*other.b)
		if isinstance(other, int):
			return self * Rational(other, 1)
	
	#Make multiplication commutative
	__rmul__ = __mul__

	def __truediv__(self, other):
		"""Division of rationals"""
		if isinstance(other, Rational):
			return self * other.recip()
		if isinstance(other, int):
			return self / Rational(other, 1)
	
	def __rtruediv__(self, other):
		"""Allows division of integers by rationals"""
		if isinstance(other, int):
			return Rational(other, 1) / self

	def __abs__(self):
		"""Return value of a/b"""
		return self.a / self.b
	
	def recip(self):
		"""Return reciprocal of self, i.e a/b -> b/a"""
		return Rational(self.b, self.a)
	
	def __pow__(self, n):
		"""Define integer powers of rationals"""
		if isinstance(n, int):
			if n > 0:
				q = 1
				for i in range(n):
					q = q*self
				return q
				
			if n == 0:
				return Rational(1,1)
				
			if n < 0:
				q = 1
				for i in range(-n):
					q = q*self.recip()
				return q
