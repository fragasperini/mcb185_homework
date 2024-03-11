#72kmercount.py by Francesca C. Gasperini

import mcb185
import sys
import gzip

k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
for kmer, n in kcount.items(): print(kmer, n)

# unsure of output with | wc

'''
Once we get to k = 7  there is one k-mer missing:
To find it do the following:
'''

import itertools
for nts in itertools.product('ACGT', repeat=k):
	kmer = ''.join(nts)
	if kmer in kcount: print(kmer, kcount[kmer])
	else:              print(kmer, 0)
# output strano, controllare il file letto