# pylint: disable=unused-variable

"""Class of quadratic irrationals"""

#Imports
from .Rational import Rational

class QuadIrrational():
	def __init__(self, r, s, d):
		"""Constructor for a Quadratic Irrational"""
		if isinstance(r, Rational) and isinstance(s, Rational) and isinstance(d, int):
			self.r = r
			self.s = s
			self.d = d
		if isinstance(r, int) and isinstance(s, int) and isinstance(d, int):
			self.r = Rational(r, 1)
			self.s = Rational(s, 1)
			self.d = d

	def __eq__(self, other):
		"""Equality of Quadratic Irrationals"""
		if isinstance(other, QuadIrrational):
			if other.r == self.r and other.s == self.s and other.d == self.d:
				return True
			else:
				return False
		if isinstance(other, Rational) or isinstance(other, int):
			if self.s == 0 and self.r == other:
				return True
			else:
				return False
		

	def __abs__(self):
		"""evaluates quadratic irrational, i.e. returns the value""" 
		return abs(self.r) + abs(self.s)*(self.d**0.5)
		
	def __repr__(self):
		"""formats nicely"""
		return "{self.r}+{self.s}\u221a{self.d}".format(self=self)
	
	def __add__(self, other):
		"""Addition of Quadratic Irrationals with various other types"""
		if isinstance(other, QuadIrrational):
			if self.d == other.d:
				return QuadIrrational(self.r + other.r, self.s + other.s, self.d)
			else:
				print("Quadratic Components must be equal")
		
		if isinstance(other, Rational) or isinstance(other, int):
			return QuadIrrational(self.r, self.s, self.d) + QuadIrrational(other, 0, self.d)
	
	#Make addition commutative
	__radd__ = __add__
	
	def __sub__(self, other):
		"""Subtraction of Quadratic Irrationals with various other types"""
		if isinstance(other, QuadIrrational):
			if self.d == other.d:
				return QuadIrrational(self.r - other.r, self.s - other.s, self.d)
			else:
				print("quadratic components must be equal")
		if isinstance(other, Rational) or isinstance(other, int):
			return QuadIrrational(self.r, self.s, self.d) - QuadIrrational(other, 0, self.d)
	
	def __rsub__(self, other):
		"""Subtraction of Quadratic Irrationals from rationals, ints"""
		if isinstance(other, Rational) or isinstance(other, int):
			return QuadIrrational(other, 0, self.d) - self
	
	def __mul__(self, other):
		"""Multiplication of Quadratic Irrationals with other types"""
		if isinstance(other, QuadIrrational):
			if self.d == other.d:
				return QuadIrrational(self.r*other.r + self.d*self.s*other.s, self.r*other.s + self.s*other.r, self.d)
			else:
				print("quadratic components must be equal")
		if isinstance(other, Rational) or isinstance(other, int):
			return QuadIrrational(self.r, self.s, self.d) * QuadIrrational(other, 0, self.d)
	
	#Make multiplication commutative
	__rmul__ = __mul__
	
	def recip(self):
		"""Returns reciprocal i.e. x -> 1/x"""
		size = self.r**2 - self.d*(self.s**2)
		return QuadIrrational(self.r / size, -self.s / size, self.d)
	
	def __pow__(self, n):
		"""Defines integer exponentiation of quadratic irrationals"""
		if isinstance(n, int):
			if n > 0:
				ans = 1
				for i in range(n):
					
					ans = ans * self
			
			if n == 0:
				ans = QuadIrrational(1, 0, self.d)
		
			if n < 0:
				ans = 1
				for i in range(-n):
					ans = ans * self.recip()
				
			return ans
	
	def __invert__(self):
		"""Returns conjugate, r+s*rt(d) -> r-s*rt(d)"""
		return QuadIrrational(self.r, -self.s, self.d)
	
	def isReduced(self):
		"""Check for being a reduced quadratic irrational"""
		if abs(self) > 1 and -1 < abs(~self) and 0 > abs(~self):
			return True
		return False