def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def ways(n):
    return fib(n+1)
        
print(ways(4))

#Fibonacci without recursion

def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 
  
# Driver Program 
  
print(fibonacci(7)) 


#########Program for staircase

def countWaysUtil(n, m): 
    if n <= 1: 
        return n 
    res = 0
    i = 1
    while i<= m and i<= n: 
        res = res + countWaysUtil(n-i, m) 
        i = i + 1
    return res 
      
# Returns number of ways to reach s'th stair     
def countWays(s, m): 
    return countWaysUtil(s + 1, m) 

print(countWays(10,2))


####################another
def stepPerms(n):
    mem = [0]*(n+1)
    return fibo(n,mem)

def fibo(n,m):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif m[n] == 0:
        m[n] = fibo(n-1,m) + fibo(n-2,m) + fibo(n-3,m)
    return m[n]
