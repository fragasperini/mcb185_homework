# 57birthday.py by Francesca C. Gasperini

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def same_birthday(trials, days, people):
	calendar = []
	for day in range(1, days + 1):
		calendar.append(day)
	duplicate_birthday = 0
	
	for i in range(trials):
		birthdays = []
		for j in range(people):
			birthdays.append(random.choice(calendar))

		if match_birthdays(birthdays):
			duplicate_birthday += 1 
	
	return duplicate_birthday / trials

def match_birthdays(birthdays):
		for a in range(len(birthdays)):
			for b in range(a + 1, len(birthdays)):
				if birthdays[a] == birthdays[b]:
					return True
		return False

print(same_birthday(trials, days, people))