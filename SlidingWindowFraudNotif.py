#!/bin/python
#use heapsort for better result.
import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notification = 0
    expense = 0
    for i in range(len(expenditure)-d+1):
        x = sorted(expenditure[i:i+d])
        y = len(x)
        z = i+d
        if d%2 !=0:
            expense = x[(y//2)]
        else:
            print('ex,ex',x[y//2],x[(y//2)-1])
            expense = (x[y//2]+x[(y//2)-1])/2.0
        if z < len(expenditure):
            if expenditure[z] >= 2*expense:
                notification += 1
    return notification

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
