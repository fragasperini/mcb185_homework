# 34scoringmatrix by Francesca C. Gasperini

nts = 'ACGT'

print('   ', end='')
for c in nts: 
	print(c, end='  ')
print()

for nt1 in nts:
	print(nt1, end=' ')
	for nt2 in nts:
		if nt1 == nt2: print('+1', end=' ')
		else:          print(-1, end=' ')
	print()