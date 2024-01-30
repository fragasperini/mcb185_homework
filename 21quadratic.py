import math

import sys

def quadratic(a, b, c): 
	delta = b**2 - 4*a*c
	
	if delta < 0:
		sys.exit('error: delta must be greater than or equal to 0')
	
	x1 = (-b + math.sqrt(delta)) / (2*a)
	x2 = (-b - math.sqrt(delta)) / (2*a)

	return x1, x2
	
x1, x2 = quadratic(3, 5, 2)
print(x1, x2)                # x1 = -0.66666666666666 and x2 = -1

x1, x2 = quadratic(1, -2, 1)
print(x1, x2)                # x1 = x2 = 1

x1, x2 = quadratic(3, 4, 2)
print(x1, x2)                # error: delta must be greater than or equal to 0