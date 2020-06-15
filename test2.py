#############################################33
a = input().split()
b = input().split()

from itertools import product
print(*list(product(a,b)))