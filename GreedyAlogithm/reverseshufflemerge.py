
#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import merge
import random

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    length = len(s)//2
    merged = ''
    rev = reversed(s[0:length])
    for i in range(length):
        shuf = random.shuffle(s[length:0])
        merged = merge(rev,shuf)
        if(merged == s):
            return min(rev,shuf)
    return min(rev,shuf)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
