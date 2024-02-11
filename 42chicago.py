# 42chicago by Francesca C. Gasperini

import random
import sys

games = 10
for i in range (games):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target: 
			print(f'yay, rolled {d1} and {d2} for {target} points')

games = 10000
for i in range(games):
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	print(score)                   # final game score

# use |sort -n | uniq -c | sort -n

# 1 million trials
games = 1000000
log = games // 100 # report progress at 1% intervals
total = 0
zeroes = 0
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}')
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target: 
			score += target
	if score == 0: zeroes += 1
	total += score 
print(total / games)
print(zeroes / games)

	
# 42chicago in class
import random

for i in range(30):
	score = 0
	for number in range(2, 13):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1 + d2 == number:
			score += number
	print(score)
		
# use | sort -n | uniq -c / n 
# |sort -n | uniq c | sort -nk2
	
# how does the program calculate the 0 score?

zerogames = 0
gamesplayed = 100000
for i in range(30):
	score = 0
	for number in range(2, 13):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1 + d2 == number:
			score += number
	if score == 0: 
		zerogames +-1 

	print(zerogames/gamesplayed)


# calculation of the average score of game Chicago:

zerogames = 0
totalscore = 0
gamesplayed = 100000
for i in range(30):
	score = 0
	for number in range(2, 13):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1 + d2 == number:
			score += number
	totalscore += score
	if score == 0: 
		zerogames +-1 

	print(total score /gamesplayed)