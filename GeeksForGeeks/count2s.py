#User function Template for python3


def number0f2s(n):
    c=0
    n = str(n)
    for i in n:
        if '2' in i:
            c+=1
    print(float("1,3"))
    return c
    
def numberOf2sinRange(n):
    x=0
    for i in range(1,n+1):
        x = x+ number0f2s(i)
        print ("x is:",x , end='\t')
    return x
        

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
# } Driver Code Ends