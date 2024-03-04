# 61skewer.py by Francesca C. Gasperini

import dogma

seq = 'ACGTACGGGGGACGTACGTCCCCC'  # make small enough that can be done by hand
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	#print(i, dogma.gc_comp(s), dogma.gc_skew(s))
	print(f'{i}\t {dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')