a = int(input())
A = set(map(int, input().split()))
for i in range(int(input())):
    s, b = input().split()
    if s == 'intersection_update':
        A &= set(map(int, input().split()))
    elif s == 'update':
        A |= set(map(int, input().split()))
    elif s == 'symmetric_difference_update':
        A ^= set(map(int, input().split()))
    else:
        A -= set(map(int, input().split()))

print (sum(A))

def fun(N):
    width = len(bin(N)) - 2
    for i in range(1,N+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)

n = input()
fun(n)