#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    # Write your code here
    decrypted = []
    l = list(s.strip())
    skipped =0
    for i in range(len(l)):
        if i<len(l) and l[i].isupper() and l[i+1].islower():
            decrypted.append(l[i+1])
            decrypted.append(l[i])
        elif l[i].isupper():
            decrypted.append(l[i])
        elif l[i]=='*':
            pass
        elif l[i].islower() and l[i-1].isupper():
            pass
        elif l[i].islower():
            decrypted.append(l[i])
        elif l[i] in '123456789':
            skipped +=1
        elif l[i] in '0':
            decrypted.append(l[skipped-1])
            skipped -=1
    return ''.join(decrypted)

if __name__ == '__main__':
    s = input()
    result = decryptPassword(s)
    print(result)

    