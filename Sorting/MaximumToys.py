#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    tot = 0
    toys = 0
    prices = sorted(prices)
    for i in range(len(prices)):
        if (prices[i] < k and tot+prices[i] <= k):
            tot += prices[i]
            toys +=1
    return toys
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
