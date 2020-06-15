if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        operation, *indices = input().split()
        if operation == 'print':
            print(l)
        else:
            cmd = 'l.'+operation+'('+",".join(indices)+')'
            eval(cmd)