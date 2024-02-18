# 55colorname.py by Francesca C. Gasperini

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q): 
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

min_d = 100000
result = 'None'
with open(colorfile) as fp:
	for line in fp:
		words = line.split('\t')
		color = words[0]
		r, g, b = words[2].split(',')
		r = int(r)
		g = int(g)
		b = int (b)
		d = dtc([R, G, B], [r, g, b])
		if d < min_d:
			min_d = d
			result = color
print(result)



'''
alternative method, without using the function dtc (taxicab distance):
	d = abs(R-r) + abs(G-g) + abs(B-b)
'''