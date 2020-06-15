# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import groupby

for line in sys.stdin:
    a = line.rstrip()

t = list((len(list(c)),int(k)) for k,c in groupby (a))
print(*t)