#70demo.py by Francesca C. Gasperini

d = {}
d = dict()

d = {'dog': 'woof', 'cat': 'meaow'}
print(d)         #prints the whole thing
print(d['cat'])  #prints the value corresponding to the item

d['pig'] = 'oink'
print(d)

d['cat'] = 'miao' #changes value
print(d)

del d['cat']     #deletes an item
print(d)

#print(d['rat'])

if 'dog' in d: print(d['dog']) #searching item in dictionary

#Iteration

for key in d: print(f'{key} says {d[key]}') #it prints dog says woof pig says oink

for k, v, in d.items(): print(k, 'says', v) #same output as before

for thing in d.items(): print(thing[0], thing[1]) #bad: always unpack tuples

print(d.keys(), d.values(), list(d.values()))

# Dictionaries are designed for fast lookups

kdtable = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtable[aa]
	return kd/len(seq)
	
# Composition

seq = 'ACGT'
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1

# Sorting dictionary
'''
python3 <program.py> <file> | sort             #sorts by feature name
python3 <program.py> <file> | sort -n -k 2     #sorts the second column by number
python3 <program.py> <file> | sort -nk2        #doesn't worl
'''

for k in sorted(count): print(k, count[k])

for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)

'''
the lambda function reads the tuple item returning the second element of it.
This way it sorts by value.
'''

def by_value(tuple):
	return tuple[1]

for k, v in sorted(count.items(), key=by_value):
	print(k, v)

#K-mers
#finding missing k-mer: 
import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)
