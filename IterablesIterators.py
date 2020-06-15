# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from itertools import combinations_with_replacement, permutations
ll = []
for line in sys.stdin:
    ll.append(line.rstrip())

lenofli = int(ll[0])
stri = ll[1].split()
indices = int(ll[2])

combo = list(permutations(stri,indices))
filt = list(filter(lambda c : stri[0] in c ,combo))

print(len(filt)/len(combo))
