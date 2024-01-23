cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "r" | grep -v "[^zoncari]" | grep -E ".{4}"