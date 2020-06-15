first = '101010'
second = '111111'
sum = 0
a = first
b = second
if len(first) != len(second):
    y = max(len(first), len(second))
    x = min(len(first), len(second))
    diff = y - x
    filler = '0'*diff
    if (len(first) == x):
        a = str(filler)+first
    else:
        b = str(filler)+second

print(a, b)


def calbinary():
    finsum = ""
    carry = 0
    for i in range(len(a)-1, -1, -1):
        #or for i in reversed(range(len(a)))
        sum = int(a[i])+int(b[i])+carry
        if sum == 2:
            finsum = '0'+finsum
            carry = 1
        elif sum == 3:
            finsum = '1'+finsum
            carry = 1
        elif sum == 1:
            finsum = '1'+finsum
            carry = 0
        else:
            finsum = '0'+finsum
            carry = 0
    if sum != 0 or sum != 1:
        finsum = '1'+finsum
    if finsum.lstrip('0') == "":
        print("0")
    else:
        print(finsum)


calbinary()
