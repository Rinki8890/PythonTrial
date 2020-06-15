#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    buy = 0
    start = 1
    for i in range(len(arr)-1):
        if i==0:
            if arr[i] < arr[i+1]:
                #start+=1
                buy += start
            elif arr[i] > arr[i+1]:
                start+=1
                buy += start
            elif arr[i] == arr[i+1]:
                buy += start
        else: 
            if arr[i-1] < arr[i] and arr[i] < arr[i+1] :
                start+=1
                buy += start
            elif arr[i-1] > arr[i] and arr[i] >= arr[i+1]:
                start-=1
                buy += start
            elif arr[i-1] < arr[i] and arr[i] >= arr[i+1]:
                start += 1
                buy +=start
            elif arr[i-1] > arr[i] and arr[i+1] >= arr[i]:
                start -= 1
                buy += start
            elif arr[i-1] == arr[i] and arr[i] > arr[i+1]:
                start += 1
                buy += start
            elif arr[i-1] == arr[i] and arr[i] < arr[i+1]:
                start -= 1
                buy += start
            elif arr[i-1] == arr[i] and arr[i] == arr[i+1]:
                buy += start
    return buy
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
