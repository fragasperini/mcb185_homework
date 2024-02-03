# 31fizzbuzz by Francesca C. Gasperini

for i in range(1, 100):
	if i % 3 == 0: 
		if i % 5 == 0: print('Fizzbuzz')
		else: print('Fizz')
	elif i % 5 == 0: print('Buzz')
	else: print(i)