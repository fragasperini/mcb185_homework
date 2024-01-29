import math 

def accuracy(fn, fp, tn, tp):  
# TP is true positives, FP is false positives, TN is true negatives, FN is false negatives
	total = (fn + fp + tn + tp)
	assert(fn >= 0)
	assert(fp >= 0)
	assert(tn >= 0)
	assert(tp >= 0)
	ac = (tn + tp) / total      # Accuracy
	p = tp / (fp + tp)          # Precision
	r = tp / (fn + tp)          # Recall
	f1 = 2*p*r / (p + r)        # F1-score
	
	return ac, f1
	
print(accuracy(5, 2, 10, 15))

print(accuracy(5, 9, 78, 55))

print(accuracy(35, 0, 53, 70))

print(accuracy(0, 0, 24, 31))

print(accuracy(-3, 8, 64, 30))