import math

def entropy(a, c, g, t):
	tot = a + c + g + t
	
	assert(tot != 0)
	assert(a >= 0)
	assert(c >= 0)
	assert(g >= 0)
	assert(t >= 0)
	
	pa = a / tot
	pc = c / tot
	pg = g / tot
	pt = t / tot

	ha, hc, hg, ht = 0, 0, 0, 0
	
	if pa != 0: ha = -pa * math.log2(pa)
	if pc != 0: hc = -pc * math.log2(pc)
	if pg != 0: hg = -pg * math.log2(pg)
	if pt != 0: ht = -pt * math.log2(pt)
	
	h = ha + hc + hg + ht
	return h 


print(entropy(0.25, 0.25, 0.25, 0.25))

print(entropy(0, 1, 3, 4))

print(entropy(2, 1, 0, 0.5))

print(entropy(0, 0, 0, 0))