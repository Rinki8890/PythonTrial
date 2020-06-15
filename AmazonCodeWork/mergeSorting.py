#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(K):
    swap = 0
    if len(K)>1:
        r = len(K)//2
        L = K[:r]
        M = K[r:]

        countInversions(L)
        countInversions(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                K[k] = L[i]
                i+=1
                k+=1
            else:
                K[k] = M[j]
                j+=1
                k+=1
                swap += 1
        while i < len(L):
            K[k] = L[i]
            i+=1    
            k += 1

        while j < len(M):
            K[k] = M[j]
            j+=1
            k+= 1 
    return swap

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)
        print(result)
