#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    s = set()
    flag = False
    if a.lower() == b.lower():
        return 'YES'     
    else:
        for i in a:
            for j in b:
                print(a,b)
                if i == j:
                    flag = True
                    b = b.replace(j,'')
                    break
                elif i.upper() == j:
                    flag = True
                    b = b.replace(j,'')
                    print(b)
                    break
                else:
                    if i.islower():
                        a = a.replace(i,'')
                        flag = True
                        break
                    elif i.isupper():
                        flag = False
                        b = b.replace(j,'')
                        break
            s.add(flag)
        if (len(s) == 1 and True in s and len(b) == 0 and len(a) == 0):
            return 'YES'

        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
###########################################################################3333333

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    s = set()
    flag = False
    if (len(a)==len(b)==0):
        return "YES"
    elif len(a)==0 and len(b)!=0:
        return "NO"
    elif len(b)==0 and len(a)!=0:
        return "NO"
    for i in a:
        for j in b:
            if i == j:
                flag = True
                b = b.replace(j,"")
                break
            elif i.upper() == j:
                flag = True
                b = b.replace(j,"")
                break
            elif i.islower():
                flag = True
                a = a.replace(i,"")
                break
            else:
                flag = False
                b = b.replace(j,"")
                break
        s.add(flag)

        if(len(s)==1 and True in s):
            return "YES"
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
########################################Correct version

import math
import os
import random
import re
import sys

import sys

def f(a, b, dp):
    if len(a) < len(b):
        return False
    if b == '':
        if a.lower() == a:
            return True
        else:
            return False
    if dp[len(a)][len(b)] != None:
        return dp[len(a)][len(b)];
    if a[-1] == b[-1]:
        dp[len(a)][len(b)] = f(a[:-1], b[:-1], dp)
        return dp[len(a)][len(b)]
    else:
        if a[-1] == a[-1].upper():
            return False
        else:
            if a[-1].upper() != b[-1]:
                dp[len(a)][len(b)] = f(a[:-1], b, dp)
            else:
                dp[len(a)][len(b)] = f(a[:-1]+a[-1].upper(), b, dp) or f(a[:-1], b, dp)
    return dp[len(a)][len(b)]
            
    

def abbreviation(a, b):
    # Complete this function
    dp = [[None]*(len(b)+2) for i in range(len(a)+2)]
    x = f(a, b, dp)
    if x:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
