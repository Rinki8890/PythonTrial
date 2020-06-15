from itertools import combinations

def makeCombos(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            yield string[i:j]
#generator means using yield which causes lazy evealuation
#generator means not using lists rather using map, lambda in a way that do no create lists
#eg sum(i*i for i in range(1000000)), without creating a list, sum will be yielded.
#eg. map(i*i for i in range (100000)),　without creating a list, sum will be yielded.
def minion_game(string):
    string = string.upper()
    Stuart = 0
    Kevin  = 0
    # make words
    result = makeCombos(string)
    for i in makeCombos(string):
        if(isVowel(i)):
            Kevin+=1
        else:
            Stuart+=1

    if Stuart>Kevin:
        print("Stuart",Stuart)
    elif Stuart==Kevin:
        print("Draw")
    else:
        print("Kevin",Kevin)


def isVowel(i):
    if len(i) > 0:
        if i[0] == 'A' or i[0] == 'I' or i[0] == 'E' or i[0] == 'O' or i[0] == 'U':
            return True
    else:
        return False
    return False

if __name__ == '__main__':
    s = input()
    minion_game(s)