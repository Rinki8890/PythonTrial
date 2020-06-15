#withoutrecursion
def fact(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

#with recursion

def factr(n):
    if n == 1:
        return 1
    else :
        return n*factr(n-1)

print(factr(4))
