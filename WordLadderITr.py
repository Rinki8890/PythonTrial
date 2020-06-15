L = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
Start = 'TOON'
End = 'PLEA'
count = 0

for l in L:
    if Start == End:
        print("Successful in {} attempts".format(count))
        exit(0)
    else:
        Start = l
        count+=1