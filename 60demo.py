# 60demo.py by Francesca C. Gasperini

# Reading FASTA files

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))


# Sequence composition

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0             # positioned inside the loop because it resents in each seq
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc / len(seq))

'''
	A.thaliana:
		Chr1 0.37049915208560646
		Chr2 0.4126366876161274
		Chr3 0.37160163343251007
		Chr4 0.36786117836965293
		Chr5 0.37964078515690164
		ChrM 0.4445352957209049
		ChrC 0.3698186528497409
	C.elegans:
		I 0.36513760250524135
		II 0.35676139115410294
		III 0.3656466286510251
		IV 0.3597960420263179
		V 0.3505670494788306
		X 0.35893876030679106
		MtDNA 0.22627737226277372
	D.melanogaster:
		2L 0.41056065187528973
		2R 0.3867694339756949
		3L 0.41244103563830925
		3R 0.5116882226233116
		4 0.34055337141161635
		X 0.3925291604013219
		Y 0.29084067297466804
'''

# if-elif-else Stack

A = 0
C = 0
G = 0
T = 0
N = 0
for nt in seq:
	if   nt == 'A': A += 1
	elif nt == 'C': C += 1
	elif nt == 'G': G += 1
	elif nt == 'T': T += 1
	else:           N += 1
print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))

# List Variation

nts = 'ACGTN'   #should really be defined outside of the loop
counts = []
for i in range(len(nts)): counts.append(0)
for nt in seq: 
	if   nt == 'A': counts[0] += 1
	elif nt == 'C': counts[1] += 1
	elif nt == 'G': counts[2] += 1
	elif nt == 'T': counts[3] += 1
	else:           counts[4] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq): .4f}', end='\t')
print()

# Indexing with str.find()
nts = 'ACGTN'
counts = [0] * len(nts)  # * initializes all counts to 0
for nt in seq:
	idx = nts.find(nt)
	counts[idx] += 1
print(name, end ='\t')
for n in counts: print('f{n/len(seq):.4f}', end='\t')
print()

# Counting

nts = 'ACGTN'
print(name, end ='\t')
for nt in nts:
	print(seq.count(nt) / len(seq), end='\t')
print()

# Sliding window algorithms

w = 10   # size of window
s = 1    # step size
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]







