#52entropy.py by Francesca C. Gasperini

import sys
import math

prob = []
for arg in sys.argv[1:]:
	f = float(arg)
	assert(f > 0 and f < 1)  # otherwise assertion error 
	prob.append(float(arg))

total = 0
for p in prob: total += p
if not math.isclose(total, 1.0):
	sys.exit('error: prob must sum to 1.0')

h = 0
for p in prob:
	h -= p * math.log2(p)

print(h)
