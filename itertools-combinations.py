from itertools import combinations_with_replacement, combinations

print(list(combinations((2,3,4),2)))

n = int(input())
letters = input().split()
#letters = ((input().split()) for _ in range(n))
#print(letters)
indices = int(input())

combo = list(combinations_with_replacement(letters,indices))
F = filter(lambda x: 'a' in x,combo)
print("{0:.3}".format(len(list(F))/len(combo)))

'''M = ''.join(L).count('a')
print 1.0 - reduce(lambda x,y: x*y,[(1.0-M*1.0/(N-i)) for i in xrange(K)])'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

