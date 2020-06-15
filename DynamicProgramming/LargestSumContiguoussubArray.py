arr = [-2, -3, -4, -1, -2, -1, -5, -3]
result = []
sums = []
result = max([sum(arr[i:j]) for i in range(len(arr)) for j in range(i+1,len(arr)+1)])
'''for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
        result.append(arr[i:j])

for i in result:
    sums.append(sum(i))

print(max(sums))'''
print(result)

#################Kadane's algo below
maxi = arr[0]
mini = arr[0]
for i in range(len(arr)):
    mini = max(arr[i], mini+arr[i])
    if mini > maxi:
        maxi = mini
print(maxi)

#######################another way usin two pointers For SUB ARRAYS, brute force approach.(NOT COMBINATIONS 
# Rather permutaitons.)
# Returns true if the 
# there is a subarray 
# of arr[] with sum 
# equal to 'sum'  
# otherwise returns 
# false. Also, prints 
# the result  
def subArraySum(arr, n, sum): 
      
    # Pick a starting  
    # point 
    for i in range(n): 
        curr_sum = arr[i] 
      
        # try all subarrays 
        # starting with 'i' 
        j = i + 1
        while j <= n: 
          
            if curr_sum == sum: 
                print ("Sum found between") 
                print("indexes % d and % d" %( i, j-1)) 
                  
                return 1
                  
            if curr_sum > sum or j == n: 
                break
            else:
                curr_sum = curr_sum + arr[j] 
                j += 1
                
  
    print ("No subarray found") 
    return 0
  
# Driver program  
arr = [15, 2, 4, 8, 9, 5, 10, 23] 
n = len(arr) 
sum = 23
  
subArraySum(arr, n, sum) 

##########ONE more approach


