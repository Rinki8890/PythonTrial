L = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
Start = 'TOON'
End = 'PLEA'

First = L[0:4]
Last = L[3:]
fcount = 0
ecount=0

for x in range(4):
    c=d=0
    Temp = First[c]
    Tem = Last[d]
    for i in range (4):
        for j in range (4):
            if Start[i] == Temp[j]:
                print("Temp:",Temp[j])
                fcount+=1
                if fcount ==3:
                    Start = Temp
                    fcount=0
                    c+=1
                    print("Start",Start)
            elif fcount<3:
                if Start[i]==Tem[j]:
                    ecount+=1
                    if ecount ==3:
                        Start = Tem
                        ecount=0
                        d+=1
                        print("S:",Start)
            else:
                pass
    if Start == End:
        print(Start,End)
        break
    print(fcount,ecount)
            
            
            
            
            
            
            
            
            
            
            
            