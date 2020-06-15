 #!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    '''mini = 999999999
    arr.sort()
    li = list(combinations(arr,k))
    for i in li:
        mins = max(i)-min(i)
        if(mins<mini):
            mini = mins'''
            #sort and do max - min, no need to find max  and min as array is sorted so i+kth
    #element will always be the max and ith will always be min
    return min([arr[i+k-1]-arr[i] for i in range(len(arr)-k+1)])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    #res = list(map(str,result))
    #print(' '.join(res))

    fptr.write(str(result) + '\n')

    fptr.close()
