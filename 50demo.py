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

# Tuples

tax = ('Homo', 'sapiens', 9606)  # construct tuple
print(tax)

'''
s[0] = 'C'
tax[0] = 'human'
'''

print(tax[0])     # index of tuples
print(tax[::-1])  # slice of tuples

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)	
	return x1, x2

x1, x2 = quadratic(5, 6, 1)        # unpacked tuple: pretty
print(x1, x2)
intercepts = quadratic(5, 6, 1)    # packed tuple: ugly
print(intercepts[0], intercepts[1])

# enumerate

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

# zip 

