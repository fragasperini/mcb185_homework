Report of programs 45, 46, 47
=============================

## 45dnastats ##

The program calculates the average value based on various different roules.
The rules taken into account are the following ones:

+ [3D6](#3D6)
+ [3D6r1](#3D6r1)
+ [3D6x2](#3D6x2)
+ [4D6d1](#4D6d1)

### 3RD ###

This program rolls 3 six-sided dice. 

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
