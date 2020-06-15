arr = list(map(int,input().split(',')))
K = int(input())

for i in range(len(arr)):
    if i+K <= len(arr):
        print(max(arr[i:i+K]))