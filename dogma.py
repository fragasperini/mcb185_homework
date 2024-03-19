# Dogma.py by Francesca C. Gasperini
import math
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
		if 	 codon == 'GCT': aas.append('A')
		elif codon == 'GCC': aas.append('A')
		elif codon == 'GCA': aas.append('A')
		elif codon == 'GCG': aas.append('A')
		elif codon == 'CGT': aas.append('R')
		elif codon == 'CGC': aas.append('R')
		elif codon == 'CGA': aas.append('R')
		elif codon == 'CGG': aas.append('R')
		elif codon == 'AGG': aas.append('R')
		elif codon == 'AGA': aas.append('R')
		elif codon == 'AAT': aas.append('N')
		elif codon == 'AAC': aas.append('N')
		elif codon == 'GAT': aas.append('D')
		elif codon == 'GAC': aas.append('D')
		elif codon == 'TGT': aas.append('C')
		elif codon == 'TGC': aas.append('C')
		elif codon == 'CAA': aas.append('Q')
		elif codon == 'CAG': aas.append('Q')
		elif codon == 'GAA': aas.append('E')
		elif codon == 'GAG': aas.append('E')
		elif codon == 'GGT': aas.append('G')
		elif codon == 'GGC': aas.append('G')
		elif codon == 'GGA': aas.append('G')
		elif codon == 'GGG': aas.append('G')
		elif codon == 'CAT': aas.append('H')
		elif codon == 'CAC': aas.append('H')
		elif codon == 'ATT': aas.append('I')
		elif codon == 'ATC': aas.append('I')
		elif codon == 'ATA': aas.append('I')
		elif codon == 'CTT': aas.append('L')
		elif codon == 'CTC': aas.append('L')
		elif codon == 'CTA': aas.append('L')
		elif codon == 'CTG': aas.append('L')
		elif codon == 'TTA': aas.append('L')
		elif codon == 'TTG': aas.append('L')
		elif codon == 'AAA': aas.append('K')
		elif codon == 'AAG': aas.append('K')
		elif codon == 'ATG': aas.append('M')
		elif codon == 'TTT': aas.append('F')
		elif codon == 'TTC': aas.append('F')
		elif codon == 'CCT': aas.append('P')
		elif codon == 'CCC': aas.append('P')
		elif codon == 'CCA': aas.append('P')
		elif codon == 'CCG': aas.append('P')
		elif codon == 'TCT': aas.append('S')
		elif codon == 'TCC': aas.append('S')
		elif codon == 'TCA': aas.append('S')
		elif codon == 'TCG': aas.append('S')
		elif codon == 'AGT': aas.append('S')
		elif codon == 'ACG': aas.append('S')
		elif codon == 'ACT': aas.append('T')
		elif codon == 'ACC': aas.append('T')
		elif codon == 'ACA': aas.append('T')
		elif codon == 'ACG': aas.append('T')
		elif codon == 'TGG': aas.append('W')
		elif codon == 'TAT': aas.append('Y')
		elif codon == 'TAC': aas.append('Y')
		elif codon == 'GTT': aas.append('V')
		elif codon == 'GTC': aas.append('V')
		elif codon == 'GTA': aas.append('V')
		elif codon == 'GTG': aas.append('V')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)

## Alternative
'''
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

# Entropy
def entropy(a, c, g, t):
	tot = a + c + g + t
	
	assert(tot != 0)
	assert(a >= 0)
	assert(c >= 0)
	assert(g >= 0)
	assert(t >= 0)
	
	pa = a / tot
	pc = c / tot
	pg = g / tot
	pt = t / tot

	ha, hc, hg, ht = 0, 0, 0, 0
	
	if pa != 0: ha = -pa * math.log2(pa)
	if pc != 0: hc = -pc * math.log2(pc)
	if pg != 0: hg = -pg * math.log2(pg)
	if pt != 0: ht = -pt * math.log2(pt)
	
	h = ha + hc + hg + ht
	return h
	
# Kyte-Doolittle hydrophobicity
def hydropathy(aa):

	if   aa == 'a': result =  1.80
	elif aa == "c": result =  2.50
	elif aa == "d": result = -3.50
	elif aa == "e": result = -3.50
	elif aa == "f": result =  2.80
	elif aa == "g": result = -0.40
	elif aa == "h": result = -3.20
	elif aa == "i": result =  4.50
	elif aa == "k": result =  3.80
	elif aa == "l": result =  3.80
	elif aa == "m": result =  1.90
	elif aa == "n": result = -3.50
	elif aa == "p": result = -1.60
	elif aa == "q": result = -3.50
	elif aa == "r": result = -4.50
	elif aa == "s": result = -0.80
	elif aa == "t": result = -0.70
	elif aa == "v": result =  4.20
	elif aa == "w": result = -0.90
	elif aa == "y": result = -1.30
	else          : result = 'Amino acid unknown'
	return result