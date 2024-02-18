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

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse = True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

#list.copy()   #it is a shallow copy, doesn't copy all the data

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTUV'
print(alph)
aas = list(alph)
print(aas)

text = 'good day to you'
words = text.split()
print(words)

line = '1.41, 2.72, 3.14'
print(line.split(','))
print(line.split('\t'))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# Searching items

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

## Index

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))

## Find

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))     # returns -1 when element can't be found
# this only works in strings, so when using it in lists or tuples, first use if

#if thing in list: idx = list.index(thing)

# Return minimum value
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

vals = [1, 6, 32, 86, 48, 2.5, 0.5, 100]
result = minimum(vals)
print(result)

# Return both min and max value
def minmax(vals): 
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
result = minmax(vals)
print(result)

# Mean value

def mean(vals):
	total = 0
	for val in vals: total += val
	return total/len(vals)

result  = mean(vals)
print(result)

# Entropy in probability distribution
import math 

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
#print(entropy([0.2, 0.3, 0.5, 0]))  #fix?

# Computation of Kullback-Leibler distance between two prob. distributions

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)     #improvements
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.1)
print(dkl(p1, p2))

# Files

with open(path) as fp:            # file pointer (fp)
	for line in fp:
		do_something_with(line)

# Compressed files

import gzip
with gzip.open(path, 'rt') as fp:
	for line in fp:
		print(line, end='')

# Converting strings to numbers

i = int('42')
x = float('0.61803')

		



