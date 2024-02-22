# Dogma.py by Francesca C. Gasperini

# Transcription

def transcribe(dna):
	return dna.replace('T', 'U')

# Reverse complement
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

# Translation
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)

## Alternative

def translate(dna):
	codons = ('ATG', 'TAA')
	aminos = 'M*'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:    # need to ask if codon is present otherwise creates errors
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)

'''
### lines 38-40 can be written as:
aas.append(aminos[codons.index(codon)])
'''

# GC count

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

# GC skew

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)