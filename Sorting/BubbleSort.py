#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swap = 0
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swap += 1
    return swap,a[0],a[len(a)-1]

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    res = countSwaps(a)

    print('Array is sorted in {} swaps.'.format(res[0]))
    print('First Element:', res[1])
    print('Last Element:', res[2])