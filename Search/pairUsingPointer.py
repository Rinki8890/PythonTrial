#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, a):
    a.sort()
    j = 1
    c = 0
    i = 0
    while(i < len(a) and j < len(a)):
        print(i,j)
        diff = abs(a[j] - a[i])
        if diff == k:
            c += 1
            j += 1
            #j = len(a)-1
            #i += 1
        elif diff > k:
            #j -= 1
            i += 1
        elif diff < k:
            #i += 1
            j += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
