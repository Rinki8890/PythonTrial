def print_formatted(n):

    spacing = len(bin(n)[2:])

    for i in range(1,n+1):
        print (str(i).rjust(spacing, ' '),str(oct(i)[1:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' '))

def fun(N):
    width = len(bin(N)) - 2
    for i in range(1,N+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)

n = input()
fun(n)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)