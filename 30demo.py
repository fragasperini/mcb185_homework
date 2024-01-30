# 30demo.py by Francesca C. Gasperini

"""""
while True: 
	print('Hello')
"""""

i = 0 
while True:
	i = i +1
	print('hey', i)
	if i ==3: break

i = 0
while i < 3:
	print(i)
	i = i + 1
print ('final value of i is', i)

i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):          #for loops
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
