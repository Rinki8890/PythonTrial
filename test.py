
from itertools import product,permutations

n = (list(map(int, input().split()))[1:] for _ in range(2))
print(n)
N = [4,5,9]
print(list(product(N)))
print(list(permutations(range(3)))) 

import sys

for line in sys.stdin:
    lengthoflist = int(line[0])
    letters = line[0:lengthoflist]
    noofindices = line[lengthoflist]
    #lengthoflist = int(lengthoflist)
print(lengthoflist, letters, noofindices)
#comb = list(combinations_with_replacement(range(lengthoflist),noofindices))


def f (ihn = 2, outs = 3):
    return ihn*outs

print(f(3))

tup = (1,)+(1,)
tup = tup + tup
print(len)


if __name__ == '__main__':
    N = int(input())

    l = []
    for _ in range(N):
        operation, *indices = input().split()
        if operation == 'print':
            print(l)
        else:
            cmd = 'l.'+operation+'('+indices[:]+')'
            eval(cmd)
    
    

