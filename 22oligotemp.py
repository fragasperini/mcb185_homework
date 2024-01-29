import math

def oligotemp(a, c, g, t): 
	total = a + c + g + t
	if total <= 13:
		tm = (a + t)*2 + (c + g)*4 
	else:
		tm = 64.9 + 41*(c + g - 16.4) / total
	return tm

tm = oligotemp(2, 6, 1, 4)  # (a + c + g + t) = 13
print(tm)                   # 40

tm = oligotemp(5, 1, 3, 2)  # (a + c + g + t) < 13
print(tm)                   # 30

tm = oligotemp(8, 4, 7, 6)  # (a + c + g + t) > 13
print(tm)                   # 56.04400000000001
