#!/bin/python3

import math
#import os
import random
import re
#import sys

# Complete the countInversions function below.
def countInversions(arr):
#left to right comparisons
#swap if LEFT > RIGHT  
#else i ++
    #j = 1
    swap = 0
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j]>arr[j+1] :
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
                swap +=1
                print(arr)
        #j+=1
    return swap
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        #input array 2 1 3 1 2
        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
