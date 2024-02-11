# 43randomdna by Francesca C. Gasperini
	# Random FASTA lines generator

import random

nts = 'ACGT'
for i in range(1, 6): 
	print('>seq-', i, sep='')
	for j in range(random.randint(55, 70)):
		print(random.choice(nts), end='')
	print()

	