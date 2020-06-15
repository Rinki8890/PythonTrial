#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    result = list(abs(i[0]-i[-1]) for i in combinations(arr,2))
    return min(result)
    #return min(abs(arr[i]-arr[i+1]) for i in range(len(arr)-1))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

    #other way
    '''n,a = input(),sorted(map(int, input().split()))
    print(min(abs(x-y) for x,y in zip(a,a[1:])))'''
    '''arr.sort() # in O(n log n) time; naive approach is O(n^2)
    return min( arr[i+1] - arr[i] for i in range(len(arr)-1) )'''