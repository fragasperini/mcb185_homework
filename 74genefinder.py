
# kinda like pro-finder
# aa = 'hdiahde'

'''
profinder splits where there is an *
here we need coordinates, so not translating it first is better bc the translation causes
loss of cooridnates
'''

# use while loop to control at which point we skip in loop
seq = 'TAGTGGTGGCGCGCGTAGACGCGTAACCCCGAAATGCCCC' #(only one stop codon inthe middle)ù

for frame in range(3):
	print(frame)
	fseq = seq[frame:]
	i = 0
	while i < len(seq):
		codon = fseq[i:i+3]
		if codon == 'ATG':
		#print(fseq[i:i+3])
			start = i
			for j in range(i, len(fseq) -2, 3):
				codon = fseq[j:j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					print('found stop at', j)
					print('gene', i+1, j+3)

'''
might wanna do it in a function, to use when doing the reverse of the sequence
for the coordinates of the negative strand all the coordinates have to go backworkds 
from the positive strand. 
'''