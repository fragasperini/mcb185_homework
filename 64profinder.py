# 64profinder.py by Francesca C.Gasperini

import dogma
import sys
import gzip
import mcb185

#Reading FASTA file of DNA (input form command line):
seq = sys.argv[1]
rev = dogma.revcomp(seq) #Create reverse strand

for defline, seq in mcb185.read_fasta(seq):
	prot_len = int(sys.argv[2]) #select proteins that are at least 100aa


#Setting 3 frame translation for forward and reverse strand:
for i in range(3):
	for j in range(i, len(seq), 3):
		fs = seq[i:j+3]
		rs = rev[i:j+3]

	#Translating sequences
	aa_seq = dogma.translate(fs)
	aa_rev = dogma.translate(rs)
	beg = 'M'
	end = '*'
	prot_fs = []
	prot_rs = []

	for x in range(len(aa_seq)):
		if aa_seq[x] == beg:
			prot =''
			for k in range(x, len(aa_seq)):
				prot += aa_seq[k]
				if aa_seq[k] == end:
					prot_fs.append(prot)
					break
	for y in range(len(aa_rev)):
		if aa_rev[y] == beg:
			r_prot =''
			for z in range(y, len(aa_rev)):
				r_prot += aa_rev[z]
				if aa_rev[z] == end:
					prot_rs.append(r_prot)
					break

	print(f"Protein in frame {i + 1} (forward):")
	if prot in prot_fs:
		print(f"{prot}")
	print(f"Protein in frame {i + 1} (reverse):")
	if prot in prot_fs:
		print(f"{r_prot}")

'''
The program seemed to work alright when using a known seq and not opening the FASTA file. 
With the following seq I had the out put below: 

# Seq and rev used:
	seq = 'ATGCCCTAGGGTATATCGCGCGGGCCCCAT'
	rev = dogma.revcomp(seq) #Create reverse strand
	print(f'reverse strand:{rev}')
	
# Print statement:
	print(f"Protein in frame {i + 1} (forward):")
	if prot in prot_fs:
		print(f"{prot}")
	else:
		print('none')
	print(f"Protein in frame {i + 1} (reverse):")
	if prot in prot_fs:
		print(f"{r_prot}")
	else:
		print('none')

#Output:
	reverse strand:ATGGGGCCCGCGCGATATACCCTAGGGCAT
Protein in frame 1 (forward):
MP*
Protein in frame 1 (reverse):
MGPARYTLGH
Protein in frame 2 (forward):
none
Protein in frame 2 (reverse):
none
Protein in frame 3 (forward):
none
Protein in frame 3 (reverse):
none

I tried debugging it to avoid having a protein output if it didn't start with 'M' and end
with '*'. But I couldn't fix it.

When running the program opening a FASTA file it seems to get stuck in the nested loop
that starts in line 23.
'''