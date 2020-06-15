def checkMax(arr):
    maxVal = max(arr)
    c = 0
    for i in range(len(arr)):
        if arr[i] == maxVal:
            c+=1
    for i in range(c):
        arr.remove(maxVal)
    return max(arr)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    print(checkMax(arr))






