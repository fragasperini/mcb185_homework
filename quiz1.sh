Name: Francesca Corinna Gasperini
Linux user name: francescacorinnagasperini

gunzip -c ~/Code/MCB185/data/dictionary.gz |grep "a" | grep -E "^[mcftoua]{4,}$"
gunzip -c ~/Code/MCB185/data/dictionary.gz |grep "a" | grep -E "^[mcftoua]{4,}$" | wc -l 

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v "[^trailnb] | grep -E {.4}
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v "[^trailnb] | grep -E {.4} | wc -l

