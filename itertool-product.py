a = map(int,input().split())
b = map(int,input().split())

#mapping all the entered input to integer and outputting a map object, stored in a. same with b

from itertools import product
print(*list(product(a,b)))