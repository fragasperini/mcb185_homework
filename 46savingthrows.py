# 46savingthrows by Francesca C. Gasperini

import random

def roll_normal():
	return random.randint(1, 20)

def roll_advantage():
	roll1 = roll_normal()
	roll2 = roll_normal() 
	if roll1 > roll2: return roll1
	else:             return roll2

def roll_disadvantage():
	roll1 = roll_normal()
	roll2 = roll_normal()
	if roll1 < roll2: return roll1
	else:             return roll2

trials = 1000
for dc in range(5, 16, 5):
	n = 0
	a = 0
	d = 0
	for i in range(trials):
		if roll_normal() >= dc: n += 1		 # Normal
		if roll_advantage() >= dc: a += 1	 # Advantage
		if roll_disadvantage() >= dc: d += 1 # Disadvantage
	print(f'{dc}\t{n/trials:.3f}\t{a/trials:.3f}\t{d/trials:.3f}')