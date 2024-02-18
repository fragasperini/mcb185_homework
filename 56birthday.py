# 56birthday.py by Francesca C. Gasperini

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def random_bday(days):
	month = random.randint(1, 12)
	if month == 2: 
		day = random.randint(1, 29)
	elif month in [4, 6, 9, 11]:
		day = random.randint(1, 30)
	else:
		day = random.randint(1, 31)
	return (month, day)

def match_bday(bdays):
	for b in range(len(bdays)):
		for c in range(b + 1, len(bdays)):
			if bdays[b] == bdays[c]:
				return True
	return False

def match_probability(trials, people, days):
	duplicate_bday = 0
	for i in range(trials):
		bdays = []
		for j in range(people):
			bdays.append(random_bday(days))
		if match_bday(bdays):
			duplicate_bday += 1
	return duplicate_bday / trials
	
print(match_probability(trials, people, days))