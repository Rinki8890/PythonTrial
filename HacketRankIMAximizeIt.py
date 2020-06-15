from itertools import product
#converts input items to integer
#map takes 2 args, ist is operation to perform second is input
# requires minimum 2 inputs
K,M = map(int,input().split())
#takes no of list K times and coverts the data into int.
N = (list(map(int, input().split())) for _ in range(K))
#takes cartisan products of two list
#if lists are [3,5] and [4,8,10] then cartisan product of the series(*){multiple inputs allowed}
#as input goes will be {3,4}{3,8}{3,10}{5,4}{5,8}{5,10}
#then all these pairs are sent for processing and max is chosen
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

###############################################33
from itertools import product
a,mod = map(int,input().split())
li = (list(map(int,input().split())) for _ in range(a))
results = map(lambda x : sum(pow(i,2) for i in x)%mod, (product(*li)))
print(max(results))

#########without using short hand operations
"""from itertools import product
a,mod = map(int,input().split())
l = []
final = []
summ = []
y = []
def summing(l):
    x = 0
    for i in range(len(l)):
        p = pow(l[i],2)
        #print("sums:  ",l[i], x)
        x = x+p
        #print("summmmmm....",x)
    summ.append(x%mod) 
    return max(summ)

for i in range(a):
    l_i = map(int,input().split())
    l.append(l_i)
products = product(*l)
for i in products:
    y.append(summing(i))
print(max(y))"""