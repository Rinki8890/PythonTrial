def printSorted():
    file_object  = open("SearchPairs\\test14.txt", "r")
    f1 =file_object.readlines() 
    
    for x in f1:
        arr = list(map(int, x.split()))
        #arr.append(x)
        arr.sort()
    for i in range(len(arr)):
        if arr[i] < 793735:
            count +=1
        print(count)
  

if __name__ == "__main__":
    printSorted()