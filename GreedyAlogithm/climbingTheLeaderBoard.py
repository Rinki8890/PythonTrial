#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.

def climbingLeaderboard(scores, alice):
    ranks = {}
    result =[]
    j = 1
    for i in range(len(scores)):
        if scores[i] not in ranks.keys():
            ranks[scores[i]] = j
            j+=1
    li = sorted(ranks.keys())
    for i in range(len(alice)):
        if alice[i] in ranks.keys():
            result.append(ranks[alice[i]])
        else:
            if alice[i] > max(ranks.keys()):
                result.append(1)
            elif alice[i] < min(ranks.keys()):
                result.append(max(ranks.values())+1)
            else:
                for k in range(len(li)):
                    if alice[i] < li[k+1]:
                        #ranks[alice[i]] = ranks[k]+1
                        #result.append(ranks[alice[i]])
                        print(alice[i], '-ii->', ranks[li[k+1]])
                        result.append(ranks[li[k+1]]+1)
                        break
                    else:
                        #ranks[alice[i]] = ranks[k]-1
                        #result.append(ranks[alice[i]])
                        print(alice[i], '-ee->', ranks[li[k+1]])
                        result.append(ranks[li[k+1]]-1)
                        break
    print(ranks)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()