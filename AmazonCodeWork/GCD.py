# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):
    hcf = 0
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

if __name__ == "__main__":
    listof = [2,3,4,5,6]
    #num1 = 1 
    #num2 = 12
    res = 1
    for i in range(len(listof)-1):
        result = compute_hcf(listof[i], listof[i+1])
        if res < result:
            res = result

print("The H.C.F. is", res)