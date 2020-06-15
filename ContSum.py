def findSum(arr):
    sum = 0
    #if (n == len(arr)):
    arr = str(arr)
    while len(arr)>1:
        for i in arr:
            sum+=int(i)
        return findSum(sum)
    if len(arr) == 1:
        return int(arr)

if  __name__ =="__main__":
    #T = input()
    #n = int(input())
    arr = input()
    sum = findSum(arr)
    print(sum)
    sumi = str(sum)