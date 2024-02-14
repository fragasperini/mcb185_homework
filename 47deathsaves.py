# 47deathsaves by Francesca C. Gasperini

import random

def roll():
	return random.randint(1, 20)

trials = 100000
death = 0
stabilized = 0
revived = 0

for i in range(trials):
	failure = 0
	success = 0
	
	for j in range(5):
		# rolling dice
		death_saves = roll()
		if death_saves >= 10 and death_saves < 20:
			success += 1
		elif death_saves == 1:
			failure += 2
		elif death_saves == 20:
			revived += 1  # revieved
			break 
		else:
			failure += 1
			
		#  character alive?
		if failure >= 3:
			death += 1
			break
		elif success >= 3: 
			stabilized += 1
			break

prob_death = death / trials
prob_stabilized = stabilized / trials
prob_revived = revived / trials

print(prob_death, prob_stabilized, prob_revived)
