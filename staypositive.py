n = 4
arr = [3,-6,5,-2,1]
newarr = []

for i in  range(len(arr)):
    n += arr[i]
    newarr.append(n)
    
print(newarr)