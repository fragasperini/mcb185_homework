# 32Fibonacci by Francesca C. Gasperini

a = -1
b =  1
for i in range (1, 11):
	c = a + b
	a = b
	b = c
	print(c)