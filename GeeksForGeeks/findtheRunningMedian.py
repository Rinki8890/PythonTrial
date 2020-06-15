#!/bin/python3

import os
import sys

#
# Complete the runningMedian function below.
#
def runningMedian(a):
    #result = []
    for i in range(1,len(a)+1):
        if len(a[0:i])>1:
            temp = sorted(a[0:i])
            if len(a[0:i])%2 ==0:
                #temp = sorted(a[0:i])
                #result.append((a[(len(a[0:i])//2)]+a[(len(a[0:i])//2)-1])/2)
                #result.append(float((temp[(len(temp)//2)]+temp[(len(temp)//2)-1])/2))
                yield float((temp[(len(temp)//2)]+temp[(len(temp)//2)-1])/2)
            elif len(a[0:i])%2 !=0:
                #result.append(float(temp[(len(temp)//2)]))
                yield float(temp[(len(temp)//2)])
        else:
            #result.append(float(a[0]))
            yield float(a[0])
    #return result

if __name__ == '__main__':
    a_count = int(input())
    a = []
    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)
    result = runningMedian(a)
    print('\n'.join(map(str,result)))