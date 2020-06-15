inv_counts = 0
def mergeSort(arr, n): 
    return _mergeSort(arr) 
  
# This Function will use MergeSort to count inversions 
  
def _mergeSort(arr): 
    if len(arr) > 1 :
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
  
        _mergeSort(lefthalf)
        _mergeSort(righthalf)
    
        merge(arr,lefthalf,righthalf) 
  
# This function will merge two subarrays in a single sorted subarray 
def merge(arr, lefthalf,righthalf): 
    left = 0    # Starting index of left subarray 
    right = 0 # Starting index of right subarray 
    index = 0     # Starting index of to be sorted subarray 
    global inv_counts
    # the inv_counts will store our inventions count
    # Conditions are checked to make sure that i and j don't exceed their 
    # subarray limits. 
    lenleft = len(lefthalf)
    lenright = len(righthalf)
    while left < lenleft and right < lenright: 
  
        # There will be no inversion if lefthalf[left] <= righthelf[right] 
        arrl = lefthalf[left]
        arrr = righthalf[right]
        if arrl <= arrr: 
            arr[index] = arrl 
            index += 1
            left += 1
        else: 
            # Inversion will occur. 
            arr[index] = arrr 
            inv_counts += lenleft - left 
            index += 1
            right += 1
  
    # Copy the remaining elements of left subarray into temporary array 
    while left < lenleft:
        arr[index] = lefthalf[left]
        left += 1
        index += 1
  
    # Copy the remaining elements of right subarray into temporary array 
    while right < lenright:
        arr[index] = righthalf[right]
        right += 1
        index += 1
  
for _ in range(int(input())):
    lenarr = int(input()) 
    arr = list(map(int,input().split()))
    mergeSort(arr,lenarr)
    print(inv_counts)
    inv_counts = 0