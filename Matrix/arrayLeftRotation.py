#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(str, input().rstrip().split()))
    l = []
    l = a[d:]
    for i in a[:d]:
        l.append(i)
    print(' '.join(l))
