#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the arrayManipulation function below.

def arrayManipulation(n, queries):
    array = [0]*(n+2)
    tot = -999
    sum = 0
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        array[a] += k
        array[b+1] -= k
    for i in range(len(array)):
        sum += array[i]
        if tot < sum:
            tot = sum
    return tot


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
