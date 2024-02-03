#36poisson by Francesca C. Gasperini

import math

def poisson(n, k):
	if k == 0: return 1
	fac = 1
	for i in range(1, k + 1): 
		fac = fac * i
	
	if n > 0:
		return (n**k / fac) * (1 / math.e)**n
	else: 
		return None
	
print(poisson(5, 2))
print(poisson(-2, 8))
print(poisson(36, 21))