# Name: Francesca Corinna Gasperini
# Linux user name: francescacorinnagasperini

# Francesca C. Gasperini, Amina Muhic

#spellingbee 1
gunzip -c ~/Code/MCB185/data/dictionary.gz |grep "a" | grep -E "^[mcftoua]{4,}$"
gunzip -c ~/Code/MCB185/data/dictionary.gz |grep "a" | grep -E "^[mcftoua]{4,}$" | wc -l 

#spellingbee 2
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v "[^trailnb] | grep -E {.4}
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v [^trailnb] | grep -E {.4} | wc -l

