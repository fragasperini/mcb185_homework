# 73missingkmers.py by Francesca C. Gasperini

import mcb185
import sys
import gzip
import itertools
import dogma

k = int(sys.argv[2])
kcount = {}
seq = sys.argv[1]
rev = dogma.revcomp(seq)
for defline, seq in mcb185.read_fasta(seq):
	#for some loops that makes a bunch of k, starting at 1 and getting bigger
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1

missing_kmers = []
for nts in itertools.product('ACGT', repeat=k):
#want to compare nts, see if in kcount. if not, we found a missing one
	kmer = ''.join(nts)
	if kmer in kcount:
		continue
	else:
		missing_kmers.append(kmer)
	n_missing_kmers = len(missing_kmers)
print(n_missing_kmers)

