# 35nchoosek by Francesca C. Gasperini

def factorial(x): 
	if x == 0: return 1
	fac = 1
	for i in range(1, x + 1): 
		fac = fac * i
	return fac 

def nchoosek(n, k):
	a = factorial(n)
	b = factorial(k)
	c = factorial(n - k)
	d = a / (b * c)
	if n < k: return None
	else    : return d
	
print(nchoosek(6, 3))
print(nchoosek(6, 0))
print(nchoosek(0, 3))

# nchoosek: n!/k!(n-k)!