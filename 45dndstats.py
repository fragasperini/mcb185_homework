# 45dndstats by Francesca C. Gasperini

import random

rolls = 1000

# 3D6: roll 3 six-sided dice
total1 = 0 
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		score += d
		total1 += score
print(total1 / rolls)

# 3D6r1: roll 3 six-sided dice, re-rolling any 1s
total2 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(2, 6)
		if d == 1: d = random.randint(1, 6)
		score += d
		total2 += score
print(total2 / rolls)

# 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
total3 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2: score += d1
		if d1 < d2: score += d2
		total3 += score
print(total3 / rolls)

# 4D6d1: roll 4 six-sided dice, dropping the lowest dice roll
total4 = 0
for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	
	if d1 < d2 and d1 < d3 and d1 < d4:   score += d2 + d3 + d4
	elif d2 < d1 and d2 < d3 and d2 < d4: score += d1 + d3 + d4
	elif d3 < d1 and d3 < d2 and d3 < d4: score += d1 + d2 + d4
	else:                                 score += d1 + d2 + d3	
	total4 += score
print(total4 / rolls)