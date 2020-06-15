import sys
from itertools import *

for line in sys.stdin:
    l,k = line.split(' ')

a = list(permutations(sorted(l),int(k)))

for i in a:
    print("".join(i))