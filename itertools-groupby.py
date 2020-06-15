from itertools import groupby

#iterator tools need to be held in the list or tuple as they return iterables
#*means unpacking the list
#* treats elements of a list as an individual element.

l = "1222311"
a = [1, 2, 3]
print(*a) #This line and line below are same. putting * presents a list as string rather than a list
print(1,2,3)
print(*[1,2,3])
print(*[(len([1,1,1])),2])
g = []

for j,k in groupby (l):
    print(j,list(k))
    print(j,len(list(k)))

    #g.append(k)
#*means unpacking the list
#in group by , first element k represents key whereas second element represents count of the keys
t =  [(k, len(list(c))) for k,c in groupby(l)]
print("Mera t hai ye:",tuple(t))
print("Mera t hai ye:",*[list(t)])
print("Mera t hai ye:",*[t])

#note the difference between round and square braces.

s =  ((k, len(list(c))) for k,c in groupby(l))
print("Mera s hai ye:",tuple(s))
print("Mera s hai ye:",*[list(s)])
print("Mera s hai ye:",*[s])

print(*[(len(list(c)), int(k)) for k,c in groupby(input())])

import sys
from itertools import groupby

for line in sys.stdin:
    a = line.rstrip()

t = list((len(list(c)),int(k)) for k,c in groupby (a))
print(*t)