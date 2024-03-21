# 65transmembrane.py by Francesca C.Gasperini

import sys
import gzip
import mcb185

hydropathy = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2,
    'X': 0.0, 'B': -3.5, 'Z': -3.5, '*': 0.0
}

def average_kd(seq, beg, leng):
	region = seq[beg : beg + leng]
	kd_value = 0
	kcount = 0 #(?)
	for aa in region:
		if aa in hydropathy:
			kd_value += hydropathy[aa]
			kcount += 1
	if kcount > 0:
		return kd_value / leng 
	else:
		return 0

def transmembrane_protein(seq):
	signal_p = average_kd(seq, 0, 8) >= 2.5
	transmembrane_region = average_kd(seq, 30, 11) >= 2.0
	pro = 'P' in seq[:30] or 'P' in seq[30:41]
	
	return signal_p and transmembrane_region and not pro

def predict_prot(prot):
	transmembrane_proteins = []
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		if transmembrane_protein(seq):
			transmembrane_proteins.append(defline)

	for defline in transmembrane_proteins:	
			print(defline)


file = sys.argv[1]
with gzip.open(file, 'rt') as fp:
	predict_prot(fp)

# design a function and then call it

'''
hydrophobic region allows to have part in the membrane, needs 11 aa etc
and needs peptidic signal that allows to go to the membrane
'''
# unclear the mistake that leads to the output
