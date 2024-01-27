import math 



def quadratic(a, b, c): 
	f = b ** 2 - 4 * a * c
	return f
	
	if f >= 0:
		x = (-b + math-sqrt(f)) / 2 * a
	elif f < 0: 
		sys.exit( 'error: delta must be greater than or equal to 0')
	
	import sys

	return x
	
x = quadratic(3, 5, 2)
print (x)


x = quadratic(3, 4, 2)
print (x)

x = quadratic(10, -4, 2)
print (x)


