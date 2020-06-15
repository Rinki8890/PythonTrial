arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 38
#Note that arrays are sorted.
#minimum diff will be 50 -(40+7)
l = 0
r = len(arr2) -1
m = len(arr1)
diff = 999999999999
res1, res2 = 0, 0
while (l < m and r >= 0):
    if abs(arr1[l] + arr2[r] -x) < diff:
        res1= l
        res2 = r
        diff = abs(x - arr1[l] + arr2[r])
    if (arr1[l] + arr2[r]) > x:
        r -= 1
    elif (arr1[l] + arr2[r]) < x:
        l += 1
print(arr1[res1],arr2[res2], diff)
