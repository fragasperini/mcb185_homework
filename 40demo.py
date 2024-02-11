# 40demo by Francesca C. Gasperini
import random

# random numbers between 0 and 1
for i in range(5):
	print(random.random())

# random choice in the strings
for i in range(50):
	print(random.choice('ACGT'), end='')
print()

# random sequence with 70% AT on average
for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')
	else:       print(random.choice('CG'), end='')
print()

# random number between two end points
for i in range(3):
	print(random.randint(1,6))

# Gaussian distribution
for i in range(5): 
	print(random.gauss(0.0, 1.0)) # argument: (mean,stdv)

print('this line\n has some\n line breaks')

print('a\tb\tcat\tdogma')

print(10, 20, 30, 40, sep='\t')
print(100, 2000, 30000, 4000, sep='\t')

# f-strings
i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')

print(f'formatted string {i} {pi:.3f}')

# sys.stderr
import sys
print('logging', file=sys.stderr)

# Monte Carlo algorithms
# Pseudorandom 
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())



















