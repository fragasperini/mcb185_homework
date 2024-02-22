# test_dogma.py by Francesca C. Gasperini

# This is a unit test of the library
import dogma
print(dogma.transcribe('ACGT'))
print(dogma.revcomp('AAAAACGT'))
print(dogma.translate('ATGTAA')) # should return M* (where * is stop codon)

s = 'ACGTGGGGGCATATG'
print(dogma.gc_comp(s))
print(dogma.gc_skew(s), dogma.gc_skew(dogma.revcomp(s)))
