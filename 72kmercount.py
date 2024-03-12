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


'''
Once we get to k = 7 there is one k-mer missing:
To find it do the following:
'''

import itertools
for nts in itertools.product('ACGT', repeat=k):
	kmer = ''.join(nts)
	if kmer in kcount: print(kmer, kcount[kmer])
	else:              print(kmer, 0)

'''
	#python3 72kmercount.py ecoli.fa.gz 7 | sort -nk2 | head
	k-mer 'GCCTAGG' is missing, it does not exist in E. coli on the positive strand. 
'''
