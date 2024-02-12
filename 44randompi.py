# 44randompi by Francesca C. Gasperini

import random
import math

in_circumference = 0
out_circumference = 0

while True: 
	x = random.random()
	y = random.random()
	d = math.sqrt(x**2 + y**2)
		
	if d < 1: in_circumference += 1
	else:     out_circumference += 1
	
	pi = 4 *  in_circumference / (in_circumference + out_circumference)
	print(pi)