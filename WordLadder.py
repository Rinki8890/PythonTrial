L = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
Start = 'TOON'
End = 'PLEA'
count = 0

c=0
Temp = L[c]

while (Start != End):
    #for i in range (4):
    print("looping times ******************:")
    for j in range (4):
        print("START, Temp: ",Start,Temp)
        itr = 1
        if Start[j] == Temp[j]:
            count+=1
            if count ==3:
                Start = Temp
                c+=1
                Temp = L[c]
                count=0
                print("Start has become \"{}\" now".format(Start))
            elif (itr>=3):
                c+=1
                Temp = L[c]
                itr=1
        else:
            itr+=1
        if Start == End:
            print("Final **********",Start,End)
            break
    print(count)