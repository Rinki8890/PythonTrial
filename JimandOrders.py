#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the jimOrders function below.
l =[]
m = []

for i in range(int(input())):
    l.append(list(map(int, input().split())))

for i,j in enumerate(l):
    m.append((sum(j), i+1))

m.sort()

for i in m:
    print(i[1])


print(*(q[0]+1 for q in sorted([(i, sum(map(int, input().split()))) for i in range(int(input()))], key=lambda x: (x[1], x[0]))))
print(*[customer for (time, customer) in sorted([(sum(map(int,input().split())), i+1) for i in range(int(input()))])])
print(*(lambda s: sorted(range(1, len(s) + 1), key=lambda i: s[i - 1]))(tuple(sum(map(int, input().split())) for _ in range(int(input())))))