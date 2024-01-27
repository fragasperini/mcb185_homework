import math

def oligotemp(A, C, G, T): 
	total = A + C + G + T
	if total <= 13:
		tm = (A + T) * 2 + (C + G) * 4 
	else:
		tm = 64.9 + 41* (C + G - 16.4) / total
	return tm

tm = oligotemp(2, 6, 1, 4)  # (A + C + G + T) = 13
print(tm)                   # 40

tm = oligotemp(5, 1, 3, 2)  # (A + C + G + T) < 13
print(tm)                   # 30

tm = oligotemp(8, 4, 7, 6)  # (A + C + G + T) > 13
print(tm)                   # 56.04400000000001s
