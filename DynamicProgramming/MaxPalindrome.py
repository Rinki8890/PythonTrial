# solution explanation: https://medium.com/@carlosbf/special-palindrome-again-solution-80a31ef3c26c
# Complete the substrCount function below.
def substrCount(n, s):
    total=0
    l1 = list(s)
    l2 = list()
    pre = l1[0]
    cnt1 = 1
    for i in range(1,n):
        if l1[i] == pre:
            cnt1+=1
        else:
            l2.append({pre:cnt1})
            pre = l1[i]
            cnt1 = 1
    l2.append({pre:cnt1})
    # case #1
    for item in l2:
        for k,v in item.items():
            total+=v*(v+1)//2
    # case #2
    l_k=""
    l_v=0
    m_k=""
    m_v=0
    for item in l2:
        for k,v in item.items():
            if m_v==1:
                if l_k == k:
                    total+=min(l_v,v)
            l_k=m_k
            l_v=m_v
            m_k=k
            m_v=v
    return total

###################################################33
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            print(i,j)
            temp = s[i:j]
            
            if temp == temp[::-1]:
                print(temp, temp[::-1])
                print(True)
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


###########################################################
Really simple 3 pass solution: 1. Build a list of tuples such that the string "aaabbc" can be squashed down to [("a", 3), ("b", 2), ("c", 1)]. 2. add to answer all combinations of substrings from these tuples which would represent palindromes which have all same letters. 3. traverse this list to specifically find the second case mentioned in probelm

Here is my code:

def substrCount(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0
		
# 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans