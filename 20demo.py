# 20demo.py by Francesca C. Gasperini

import math

print('hello, again') # greetings

"""
This is a 
multi-line 
comment
"""

# Math Operators 

print(1.5e-2)
print(1 + 1)
print(2 * 2)
print(2 ** 3)	# exponential
print(5 // 2)	# integer divide
print(5 % 2)	#modulo, provides remainder after integer division

# Math functions

print(abs(-3)) 	# absolute value of -3
print(pow(3, 2)) 	# 3 to the power of 2
print(round(3.658318, ndigits=3))	# round off x to 3 digits
print(math.log10(101))
print(math.sqrt(36))	# square root of 36
print(math.e)
print(math.inf)

# Number approximations

print(0.1*1)
print(0.1*3)

# Pythagorean theorem

a = 3						# side of triangle
b = 4						# side of triangle
c = math.sqrt(a**2 + b**2)	# hypotenuse
print(c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ')

# Functions

def greeting():						# def only creates the function, it does not run it 
	print('hello yourself')
	
def pythagoras(a, b):	
	c = math.sqrt(a**2 + b**2)
	return c
	
x = pythagoras(3, 4)
print(x)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3, 4))
print(pythagoras(1, 1))	

def pythagoras(a, b):
	assert(a > 0)
	assert(b > 0)
	return math.sqrt(a**2 + b**2)

def pythagoras(a, b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**s + b**s)


# Practice 


#  Strings

s = 'hello world'
print(s, type(s))

# Conditionals

a = 2
b = 2
if a == b:
	print('a equals b')
	
a = 2
b = 6
if a == b:
	print('a equals b')

if a == b: 
	print('a equals b')
print(a, b)


# Boolean 

c = a == b
print(c)			# Boolean value can either be true or false
print(type(c))

a = 3
b = 3
c = a == b
print(c)
print(type(c))

if a < b:
	print('a < b')
elif a > b: 
	print('a > b')
else:
	print('a == b')

# if simple format as follows: 

if		a < b: print('a < b')
elif	a > b: print('a > b')
else:			print('a == b')	

# Chaining

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world ')
if not False: print(True)

# Errors in equity with floating points

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')
	# program reports a < b which is wrong
	
print(abs(a - b))	# 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

# String comparison

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

# Mismatched type error

a = 1
s = greeting
if a < s: #print('a < s') 
	# '<' not supported between instances of 'int' and 'function'

# More practice


# Spacing

if   nt == 'A': comp = 'T'
elif nt == 'C': comp = 'G'
elif nt == 'G': comp = 'C'
elif nt == 'T': comp = 'A'
else:           sys.exit('unkown nucleotide', nt)
