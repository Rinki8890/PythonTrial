import sys
import math

register = {.01:'PENNY',.05:'NICKEL',.10:'DIME',.25:'QUARTER',.50:'HALF DOLLAR',1.00:'ONE',2.00:'TWO',5.00:'FIVE',\
           10.00:'TEN',20.00:'TWENTY',50.00:'FIFTY',100.00:'ONE HUNDRED'}
denos = [i for i in register.keys()]
#Greater value to findout the diff with max denom
denos.sort(reverse=True)
result = []
diff = .00

def findchange(change):
    #global diff
    for i in denos:
        if change > i:
            diff = round((change - i),2)
            result.append(register[i])
            break
    if diff in denos:
        result.append(register[diff])
        return result
    else:
        return findchange(diff)
            
    return result

def calculateChange(pp,ch):
    if pp < ch:
        change = round((ch - pp),2)
        #If denomination is available for the change then return it
        #Else calculate the change to be returned in available denominations.
        if change in register.keys():
            print(register[change])
        else :
            result = findchange(change)
            print((",").join(result))
    elif pp>ch :
        print('ERROR')
    else:
        print('ZERO')
    

if __name__ == '__main__':
    inputs = list(map(float,input().split(';')))
    a = inputs[0]
    b = inputs[1]
    
    calculateChange(a,b)