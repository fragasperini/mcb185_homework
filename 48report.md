Report of programs 45, 46, 47
=============================

## 45dnastats ##

The program calculates the average value based on various different roules.
The rules taken into account are the following ones:

+ [3D6](#3D6)
+ [3D6r1](#3D6r1)
+ [3D6x2](#3D6x2)
+ [4D6d1](#4D6d1)


### 3R6 ###

This program rolls 3 six-sided dice and then calculates the average
of the throws. 

```
import random

rolls = 1000
total1 = 0 
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		score += d
		total1 += score
print(total1 / rolls)
```

The resulting average is: 20.829


### 3D6r1 ###

This program rolls 3 six-sided dice, re-rolling any time the number
rolled is 1. 

```
import random

rolls = 1000
total2 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(2, 6)
		if d == 1: d = random.randint(1, 6)
		score += d
		total2 += score
print(total2 / rolls)
```

The resulting average is: 24.373


### 3D6x2 ###

This program rolls pairs of six-sided dice 3 times, taking the
maximum each time. 

```
import random

rolls = 1000
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
```

The resulting average is: 26.678


### 4D6d1 ###

This program rolls 4 six-sided dice, dropping the lowest roll. 

```
import random

rolls = 1000
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
```

The resulting average is: 11.767


## 46savingthrows ##

A saving throw determines success in certain events. Rolling a d20 
there are different levels od difficulty, called difficulty classes 
(DC) that regulate wether success is acieved or not.
For exapmle dc 5 means that scoring 5 or higher grants success. 
Some events can grant advantage, which consists in rolling two dice
and keeping the higher score or disadvantage, rolling two dice and 
keeping the lower number. This program simulates saving throws
against DCs 5, 10 and 15 and calculates the probability of success 
in normal conditions, with advantage or disadvantage.

| DC | Normal | Adv. | Disadv. |
|:--:|:------:|:----:|:-------:|
|  5 |  0.751 |      |         |
| 10 |  0.497 |      |         |
| 15 |  0.263 |      |         |

_Note: in the terminal there is no output for conditions of advantage 
or disadvantage, which is also why those two columns, in the table 
above, are empty. I think that it is due to a mistake in the way I 
structured the loops but I have been unable to fix it._

## 47deathsaves ##


 