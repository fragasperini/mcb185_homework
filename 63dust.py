#63dust.py by Francesca C. Gasperini

import sys
import mcb185
import dogma

# Reading command line
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	w = int(sys.argv[2])
	ent_threshold = float(sys.argv[3])

# When to mask a sequence
masked_seq = ''
for i in range(0, len(seq) -w +1, w):
	window = seq[i:i+w]
	a = window.count('A')
	c = window.count('C')
	g = window.count('G')
	t = window.count('T')
	h = dogma.entropy(a, c, g, t)
	if h < ent_threshold: masked_seq += 'N' * w
	else:                 masked_seq += seq[i:i+w]
print(defline)

for i in range(0, len(masked_seq), 60): #this wrapps the loop 
	print(masked_seq[i:i+60] )
	
#outputs should look like fasta files, with entries and everything
'''
low complexity is a threshold (usually needed a bunch of ATs). 
Need to do a substitution of the actual sequence with N. The more N the more
alignments will not work.

for strings just create an empty one and then add stuff to it 
'''
'''
aviod making as many Ns as possible(?)
convert the string? take dna making it to something else
doing a list 
put sequence into list
seq.split()
area of low  complexity vjangfe it 
no need to nest a loop
'''