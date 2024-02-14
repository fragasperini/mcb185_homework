Report of programs 45, 46, 47
=============================

## 45dnastats ##

The program calculates the average value based on various different 
rules.
The rules taken into account are the following ones:

+ [3D6](#3D6)
+ [3D6r1](#3D6r1)
+ [3D6x2](#3D6x2)
+ [4D6d1](#4D6d1)


### 3D6 ###

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

| DC | Normal |  Adv.  | Disadv. |
|:--:|:------:|:------:|:-------:|
|  5 |  0.819 |  0.959 |  0.622  |
| 10 |  0.539 |  0.795 |  0.322  |
| 15 |  0.295 |  0.527 |  0.090  |


## 47deathsaves ##

In death saves if the throw of a d20 results in a number lower than
10 the result is one "failure". If the number equals to 10 or greater 
you score a "success". 3 failures result in "death", while 3 successes
result in "stabilization". When rolling a 1, it counts as 2 failures,
while rolling a 20 results in being revived. The program simulates 
death saves and the probability of the throws resulting in death,
stabilizing or being revived. 

|  Condition |     Rolls    | Probability |
|:----------:|:------------:|:-----------:|
|    Death   | failure >= 3 |    0.40574  |
| Stabilized | success >= 3 |    0.40936  |
|   Revived  |    roll 20   |    0.1849   |

