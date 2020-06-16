import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    n = n*k
    if n%9 == 0:
        return 9
    else:
        return n%9

    #ternary condition
    #return 9 if n%9 == 0 else n%9

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()