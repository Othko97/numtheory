# pylint: disable=unused-variable

"""Just some stuff to find some number theory stuff"""
#Imports
from .QuadIrrational import QuadIrrational
from .Rational import Rational, euclid
from .SimpleContFrac import SimpleContFrac, exeuclid
from .PeriodicContFrac import PeriodicContFrac
print('linea;sdlkfjas;fj ')
def flt_ratio(flt):
	"""Return rational number with decimal expression flt"""
	return Rational(int(flt * (10**len(str(flt)))), (10**len(str(flt))))

#def solvepell(d):
	#"""Returns Fundamental nontrivial positive solution for Pell's Equation:
	#x^2 - d*y^2 = 1"""
	#if int(d**0.5)**2 == d:
	#	print("No solutions")
	#else:
		#rootd = QuadIrrational(0, 1, d)
		#confrac = rootd.contfracrep()
		#exconfrac = confrac + confrac[1:]
		#r = len(confrac)
		#if r % 2 == 0:
		#	s = 2 * r - 1
		#else:
		#	s = r - 1
		#frac = Rational(1,1)#simplecontfrac(exconfrac[:s])
		#print(frac.a**2 - d*(frac.b**2))
		#return (frac.a, frac.b)
		
	

def totient(n):
	"""awful inefficient implementation of Euler's totient function"""
	c = 0
	#find how many numbers less than n are coprime with n
	for i in range(1, n):
		if euclid(i, n) == 1:
			c += 1
	return c

def checkprime(p):
	"""checks if p prime"""
	#check if there is a divisor less than the square root of p
	for i in range(2, int(p**0.5)+1):
		if p % i == 0:
			return False
	#if not return true 
	else:
		return True
	
	
def primefactor(n):
	"""finds all prime factors of n"""
	#if prime can just return itself
	if checkprime(n):
		return [n]
	#if not prime find a prime divisor
	else:
		for i in range(2, int(n**0.5)+1):
			if n % i == 0 and checkprime(i):
				return [i] + primefactor(int(n/i))	#recursively return divisor, primefactors of quotient
	

def findunits(n):
	"""finds the group of units modulo n"""
	units = []
	#find numbers coprime with n less than or equal to n 
	for i in range(1, n):
		if euclid(i, n) == 1:
			units.append(i)
	return units
	
def findquads(n):
	"""finds quadratic residues modulo n"""
	#square every unit
	return list(set([i**2 for i in findunits(n)]))

def findprims(n):
	"""finds primitive roots modulo n"""
	units = findunits(n)
	primitives = []

	#for each unit check if primitive
	for i in units:
		flag = False

		#for each prime divisor q of order of units |U|
		for q in primefactor(len(units)):

			#check i does not have order |U|/q
			if i ** (len(units)/q) % n == 1:
				flag = True
				
		if flag == False:
			primitives.append(i)
	return primitives

def legendre(a, p):
	"""computes legendre symbol (a/p)"""
	if a % p == 0:
		return 0
	elif a in findquads(p):
		return 1
	else:
		return -1


