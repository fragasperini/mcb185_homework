# 44randompi by Francesca C. Gasperini

import random
import math

r = 0
b = 0

while True: 
	x = random.random()
	y = random.random()
	d = math.sqrt(x**2 + y**2)
	
	if d < 1: r += 1
	else:     b += 1
	
	pi = 4 * r / (r + b)
	print(pi)

	