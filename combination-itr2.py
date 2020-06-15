from itertools import permutations,combinations, combinations_with_replacement

print (list(permutations([1,2,3],2)))

print (list(combinations([1,2,3],2)))

n = input().split()

letters = n[0].split()
letters = ("").join(letters)
print(letters)
a =[]
ind = int(n[1])
for i in range(len(letters)):
    a.append(letters[i])
a.sort()
l = list(combinations_with_replacement(a,1))
print(*l)
l = list(combinations_with_replacement(a,ind))
f = list(filter(lambda x: x[0]!=x[1],l))
un = filter(lambda x: x[0]!=x[1],l)
#print(m)   
print(*l) 

for i in un:
    print("".join(i))
