a = input().split()
#inout Hack 2
from itertools import combinations
for i in range(1,int(a[1])+1):
    c = combinations(sorted(a[0]),i)
    for combs in c:
        print(''.join(combs))