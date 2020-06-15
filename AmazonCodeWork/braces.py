#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    opening = []
    closing = []
    if len(s)%2!=0:
        return 'NO'
    else:#stack imple
        for i in s:
            if i in '{([':
                opening.append(i)
            else:
                closing.append(i)
        if len(opening)!=len(closing):
            return 'NO'
        else:
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
