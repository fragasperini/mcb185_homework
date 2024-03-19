# 62skewer.py by Francesca C.Gasperini

import sys
import mcb185
import gzip
import dogma

seq = sys.argv[1]
wlen = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]): # setting initial position
	g = seq[:wlen].count('G')
	c = seq[:wlen].count('C')

	for i in range(len(seq) -wlen): #no +1 because it would go out of range
		drop = seq[i]
		gain = seq[i + wlen]
	
		if drop == 'C'  : c -= 1
		elif drop == 'G': g -= 1
		if gain == 'C'  : c += 1
		elif gain == 'G': g += 1
		s = seq[i + 1:i+wlen + 1]
		
		# calculate the output without calling functions
		gc_comp = (g + c) / wlen
		gc_skew = (g - c) / (g + c) if(g + c) != 0 else 0

		print(f'{i}\t {gc_comp}\t{gc_skew}')

'''
#61skewer.py
for defline, seq in mcb185.read_fasta(sys.argv[1]):

	for i in range(0, len(seq) -wlen +1, 1):   
	# not adding one bc we are looking 1 ahead
		s = seq[i:i+wlen]
		print(f'{i}\t {dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
		
# ideal solution to dust as well(?)
'''

'''
## Timing of the programs ##

|  wlen | 61.skwer | 62.skwer |
|:-----:|:--------:|:--------:|
|    10 |  4.42 s  |  3.56 s  |
|   100 |  4.79 s  |  3.86 s  |
|  1000 | 10.14 s  |  4.70 s  |
| 10000 | 60.75 s  |  5.25 s  |

'''