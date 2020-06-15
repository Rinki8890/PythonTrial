s = ""
def reverseit(instring):
    global s
    if len(instring) > 1:
        s+=instring[-1]
        return reverseit(instring[:-1])
    else:
        s+=instring
        return s

print(reverseit("akshay"))