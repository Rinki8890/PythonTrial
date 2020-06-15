#!/bin/python
def median(a,x): 
    temp = []
    c=0
    for i in a:
        if i == "r":
            if len(temp)!=0 and c < len(temp):
                temp.pop(x[c])
        else:
            temp.append(x[c])
        c+=1
    
    for i in range(1,len(temp)+1):
        if len(temp[0:i])>1:
            tmp = sorted(temp[0:i])
            if len(a[0:i])%2 ==0:
                yield float((tmp[(len(temp[0:i])//2)]+tmp[(len(temp[0:i])//2)-1])/2)
            else:
                yield float(tmp[(len(temp[0:i])//2)])
        elif len(temp[0:i])==1:
            yield float(temp[0])
        else:
            yield "Wrong!"


N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
result = median(s,x)
print("\n".join(map(str,result)))