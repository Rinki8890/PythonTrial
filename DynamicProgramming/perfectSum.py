arr = [15, 2, 4, 8, 9, 5, 10, 23]
K = 23
total = 0
res = []
from itertools import combinations
for i in range(1,len(arr)):
    subarr = list(combinations(arr,i))
    for j in subarr:
        if sum(j) == K:
            print(j)

