# 53genomestats by Francesca C. Gasperini

import sys
import gzip

#pathway to file
gffpath = sys.argv[1]
feature = sys.argv[2]

vals = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] != '#':
			words = line.split()
			if words[2] == feature:
				beg = int(words[3])
				end = int(words[4])
				vals.append(end - beg + 1)

# minimum
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

# maximum
def maximum(vals):
	maxi = vals[0]
	for val in vals[1:]:
		if val > maxi: maxi = val
	return maxi

# mean
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

# standard deviation
def st_dev(vals):
	total = 0
	for val in vals: 
		total += val
	mean = total / len(vals)
	
	tot = 0
	for val in vals: 
		tot += (val - mean)**2
	return (tot / len(vals) - 1)**0.5

# median
def median(vals):
	vals.sort()
	if len(vals) % 2 == 0:
		mid = len(vals) // 2
		med = (vals[mid - 1] + vals[mid]) / 2  # even lists
	else:
		med = vals[len(vals) // 2]             # odd lists
	return(med)


print('length:', len(vals))
print('minimum:', minimum(vals))
print('maximum:', maximum(vals))
print('mean:', mean(vals))
print('standard deviation:', st_dev(vals))
print('median:', median(vals))

