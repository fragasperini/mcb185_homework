# nilakantha by Francesca C. Gasperini

def nilakantha(limit):
	for i in range(2, limit): 
		a = i * 2
		b = a + 1
		c = b + 2
		
		if i % 2 == 0: sign = '-'
		else:          sign = '+'
	print(a, b, c, sign)

	number = 4 / (a * b * c)
	
	if sign == '-': return -number
	else:           return +number
	
	return 3 + number
	
#limit = 10
#print(nilakantha(limit))