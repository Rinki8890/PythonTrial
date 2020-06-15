#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    li = set()
    x = a.upper
    if b in a:
        li.add(1)
    else : 
        for i in b:
            if i in a or i in x:
                li.add(1)
            else:
                li.add(0)
    yield li


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()
        
        result = abbreviation(a, b)
        result = list(map(set, result))
        if len(result) == 1 and result[0] == 1:
            print('YES')
        else:
            print('NO')

        #fptr.write(result + '\n')

    #fptr.close()
