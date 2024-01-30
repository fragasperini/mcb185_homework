import math

def hydropathy(aa):
#function returns correspondence between aa and Kyte-Doolittle hydrophobicity value

	if   aa == 'a': result =  1.80
	elif aa == "c": result =  2.50
	elif aa == "d": result = -3.50
	elif aa == "e": result = -3.50
	elif aa == "f": result =  2.80
	elif aa == "g": result = -0.40
	elif aa == "h": result = -3.20
	elif aa == "i": result =  4.50
	elif aa == "k": result =  3.80
	elif aa == "l": result =  3.80
	elif aa == "m": result =  1.90
	elif aa == "n": result = -3.50
	elif aa == "p": result = -1.60
	elif aa == "q": result = -3.50
	elif aa == "r": result = -4.50
	elif aa == "s": result = -0.80
	elif aa == "t": result = -0.70
	elif aa == "v": result =  4.20
	elif aa == "w": result = -0.90
	elif aa == "y": result = -1.30
	else          : result = 'Amino acid unknown'
	return result
	
aa = 'a'
result = hydropathy(aa)
print(result)

aa = 'g'
result = hydropathy(aa)
print(result)

aa = 'x'
result = hydropathy(aa)
print(result)

aa ='h'
result = hydropathy(aa)
print(result)