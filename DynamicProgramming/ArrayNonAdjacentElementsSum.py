def maxsubsetsum(arr):    
    dp = {} # key : max index of subarray, value = sum
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
    return dp[len(arr)-1]	


def maxSubsetSum(arr):
    subset = [arr[0],max(arr[0],arr[1])]
    for i in range(2,len(arr)):
        subset.append( max(subset[i-1],subset[i-2],arr[i],arr[i]+ subset[i-2]))
        print(subset)
    return max(subset)