arr = [2,3,5]
product = 1
#substr = set()
for i in range(len(arr)):
    res = 1
    for j in range(i, len(arr)):
        '''for j in range(i+1, len(arr)+1):
        substr = arr[i:j]
        print(substr)
        for x in substr:
            product *= x 
            Or below is better'''
        print(arr[j])
        res *= arr[j]; 
        product = res * product 
print(product)
