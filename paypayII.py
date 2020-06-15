import sys
register = {.01: 'PENNY', .05: 'NICKEL', .10: 'DIME', .25: 'QUARTER', .50: 'HALF DOLLAR', 1.00: 'ONE', 2.00: 'TWO', 5.00: 'FIVE',
            10.00: 'TEN', 20.00: 'TWENTY', 50.00: 'FIFTY', 100.00: 'ONE HUNDRED'}
dno = [i for i in register.keys()]
dno.sort(reverse=True)
result = []
safe = .00


def findchange(change):
    global safe
    for i in dno:
        if i < change:
            safe = change - i
            safe = round(safe, 2)
            result.append(register[i])
            break
    if safe in dno:
        result.append(register[safe])
        return result
    else:
        return findchange(safe)

    return result


line = [35.0, 189.91]
PP = float(line[0])
CH = float(line[1])

if (CH < PP):
    print("ERROR")
elif (CH == PP):
    print("ZERO")
else:
    change = float(CH - PP)
    change = round(change, 2)
    if change in register:
        print(register[k])
    else:
        # Take all the keys in a separate list
        # break up the change into available denominations
        result = findchange(change)
        results = (",").join(result)
        print(results)

#if __name__ == "__main__":
