#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def matchingbraces(b):
    if b == '}':
        return '{'
    elif b == ')':
        return '('
    elif b == ']':
        return '['

def isBalanced(s):
    leng = len(s)
    #s = list(s)
    print(s)
    stack = []
    openi = opening = ''
    #if bracket in open then look for closing
    if len(s)%2 != 0:
        return 'NO'
    else:
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                openi = matchingbraces(i)
                if len(stack)==0:
                    return 'NO'    
                else:
                    opening = stack.pop()
                    if opening == openi:
                        continue
                    else:
                        return 'NO'
        if len(stack) == 0:
            return 'YES' 
        return 'NO'   
            

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)
