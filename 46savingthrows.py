# 46savingthrows by Francesca C. Gasperini

import random

def roll_normal():
	return random.randint(1, 20)

# Normal

trials = 1000
print('dc', 'norm', 'adv', 'dis', sep='\t')
for dc in range(5, 16, 5):
	print(dc, end= '\t')
	success = 0 
	for i in range(trials):
		rn = roll_normal()
		if rn > dc: success += 1
	print(success / trials)

# Advantage

def roll_advantage():
	roll1 = roll_normal()
	roll2 = roll_normal() 
	if roll1 > roll2: return roll1
	else:             return roll2

	for i in range(trials):
		rn = roll_advantage()
		if rn > dc: success += 1
	print(success / trials)

# Disadvantage

def roll_disadvantage():
	roll1 = roll_normal()
	roll2 = roll_normal()
	if roll1 < roll2: return roll1
	else:             return roll2
	
	for i in range(trials):
		rn = roll_disadvantage()
		if rn > dc: success += 1
	print(success / trials)
	print(f'{dc}\t{n/trials:.3f}\t{a/trials:.3f}\t{d/trials:.3f}')

