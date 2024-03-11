#71countgff.py by Francesca C. Gasperini

import sys
import gzip

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 1
		else:                    count[feature] += 1
		
#for f, n in count.items(): print(f, n)

'''
Alternative for lines 12 and 13: 
	if feature not in count: count[feature] = 0
	count[feature] += 1

Equivalent of the following command line: 
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 |

Various keys can be sorted with following command lines: 

python3 71countgff.py ecoli.gff.gz | sort
	CDS 4337
	exon 207
	gene 4494
	mobile_genetic_element 50
	ncRNA 99
	origin_of_replication 1
	pseudogene 145
	rRNA 22
	region 1
	sequence_feature 48
	tRNA 86

python3 71countgff.py ecoli.gff.gz | sort -n -k 2
	origin_of_replication 1
	region 1
	rRNA 22
	sequence_feature 48
	mobile_genetic_element 50
	tRNA 86
	ncRNA 99
	pseudogene 145
	exon 207
	CDS 4337
	gene 4494

python3 71countgff.py ecoli.gff.gz | sort -nk2
(output is the same as previous one)

It is also possible to sort inside python, like follow: 
'''
#Sorting
#for k in sorted(count): print(k, count[k])

#Sorting by value
for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)

#Explanation of sorting by value
def by_value(tuple):
	return tuple[1]

for k, v in sorted(count.items(), key=by_value):
	print(k, v)