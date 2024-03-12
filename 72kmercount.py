#72kmercount.py by Francesca C. Gasperini
import mcb185
import sys
import gzip
import itertools

k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
#for kmer, n in kcount.items(): print(kmer, n)
'''
for k = 7 we get 16383 kmers instead of 16384
one kmer is missing
To know which one is different do like follow: 
'''
for nts in itertools.product('ACGT', repeat=k):
	kmer = ''.join(nts)
	if kmer in kcount: print(kmer, kcount[kmer])
	else:              print(kmer, 0)

'''
Running the program as follows: 
python3 72kmercount.py ecoli.fna.gz 7 | sort -nk2 | head
The kmer GCCTAGG 0 is absent on the positive strand. 
Now in the output there are 16384 kmers.
'''
