n = int(input())

required = input().split()
stock = input().split()

required = [int(i) for i in required]
stock = [int(i) for i in stock]

l = []

for i in range(0,n):
    a_i = stock[i]//required[i]
    l.append(a_i)

#l.sort()

print(min(l))