''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    T = 1
    """numb = input()
    blades = input()
    opponents = input()
    blades_list = list(blades.split())
    blades_list.sort(reverse=True)"""
    """blades_list = [int(i) for i in blades_list]
    opp_list = list(opponents.split())
    opp_list.sort(reverse=True)
    opp_list = [int(i) for i in opp_list]"""
    opp_list = [23,34]
    blades_list = [24,20]
    print(len(opp_list),len(opp_list))
    win_g = 0

    while(T>0):
        T-=1
        for i in range(0,len(blades_list)):
            #print("i is ",i)
            for j in range(0,len(opp_list)):
                #print("j is ",j)
                if (blades_list[i]) > (opp_list[j]):
                    win_g +=1
                    opp_list.pop(j)
                '''elif blades_list[i] == opp_list[j]:
                    #print("i,",i)'''
                
    return win_g



main()

