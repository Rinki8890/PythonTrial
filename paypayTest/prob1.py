import sys

def compute(a,b):
    binsum = ''
    carry = 0
    first = a
    second = b
    #comparing length of two lists and padding if not equal
    if (len(first) != len(second)):
        y = max(len(first), len(second))
        x = min(len(first), len(second))
        diff = y - x
        filler = '0'*diff
        if (len(first) == x):
            a = str(filler)+first
        else:
            b = str(filler)+second
      
    for i in range(len(a)-1,-1,-1):
        tot = int(a[i])+int(b[i])+carry
        if tot == 2:
            binsum = '0'+binsum
            carry = 1
        elif tot == 3:
            binsum = '1'+binsum
            carry = 1
        elif tot == 1:
            binsum = '1'+binsum
            carry = 0
        else:
            binsum = '0' + binsum
            carry = 0
    #if tot != 1 or tot!= 0:
        #binsum = '1' + binsum
    if binsum.lstrip('0') == '':
        print(0)
    elif binsum[0] == '0':
        print(binsum.lstrip('0'))
    else :
        print(binsum)
        

if __name__ == '__main__':
    a,b = input().split(',')
    compute(a,b)
    
    