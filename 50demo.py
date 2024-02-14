# 50demo by Francesca C. Gasperini

# Indexes

seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

# Slices

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])                  # step size is 2
print(s[0:5], s[:5])             # omitting initial value
print(s[5:len(s)], s[5:])        # omitting final value
print(s[0], s[0:1])              # single element
print(s, s[::], s[::1], s[::-1]) # s[::-1] prints JIHGFEDCBA 
	# s[::-1] is used to reverse complement sequences

# Tuples

tax = ('Homo', 'sapiens', 9606)  # construct tuple, taxonomic identifier
print(tax)

'''
s[0] = 'C'       #strings cannot be changed this way
tax[0] = 'human' #same applies to tuples
'''

print(tax[0])     # index of tuples
print(tax[::-1])  # slice of tuples

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)	
	return x1, x2
x = quadratic(1, 1, 1)
print(x)

x1, x2 = quadratic(5, 6, 1)        # unpacked tuple: pretty
print(x1, x2)
intercepts = quadratic(5, 6, 1)    # packed tuple: ugly
print(intercepts[0], intercepts[1])

# enumerate

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):       # usually best one to use
	print(i, nt)

i = 0                              # do not use
for nt in nts:
	print(i, nt)
	i += 1

# zip 

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(nts)):          # or len(names) ?
	print(nts[i], names[i])

for nt, name in zip(nts, names):   # much better, error with different lenght of containers,not problem
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

# Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)