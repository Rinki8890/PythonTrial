''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    T = int(input())
    while(T>0):
        numb = input()
        blades = input()
        opponents = input()
        blades_list = list(blades.split())
        blades_list.sort(reverse=True)
        blades_list = [int(i) for i in blades_list]
        opp_list = list(opponents.split())
        opp_list.sort(reverse=True)
        opp_list = [int(i) for i in opp_list]
        win_g=0
        T-=1
        tmp_list = opp_list[:]
        for i in range(len(blades_list)):
            for j in range(len(opp_list)):
                if blades_list[i] > opp_list[j]:
                    tmp_list.pop(j)
                    win_g +=1
                    opp_list = tmp_list[:]
                    break
        print(win_g)

main()

