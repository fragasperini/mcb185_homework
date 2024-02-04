# 30demo.py by Francesca C. Gasperini

"""""
while True: 
	print('Hello')
"""""

i = 0 
while True:
	i = i +1
	print('hey', i)
	if i ==3: break                          # break breaks the loop

i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)

i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):                    # for loops
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)
	
for char in 'hello':
	print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)

for i in range(len(seq)):
	print(seq)

# Nested loops
for nt1 in 'ACGT':                            # outer loop
	for nt2 in 'ACGT':                        # inner loop
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')

nts = 'ACGT'
for nt1 in nts:
	for nts in nts: 
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')

limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)

def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': 
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total

print(gc_comp('ACAGAGATT'))

# Practice problems

# Triangular

def triangular(n): 
	tri = 0
	for i in range(n+1):
		tri = tri + i
	return tri

print(triangular(8))

# Factorial 

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

print(factorial(4))

# Euler

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e

print(euler(7))

# Perfect squares
import math 

def perfect_square(n): 
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False

print(perfect_square(4))
print(perfect_square(7))

# Prime numbers

def prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False 
	return True

print(prime(7))
print(prime(76))