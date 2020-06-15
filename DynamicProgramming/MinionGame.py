from itertools import *


def minion_game(string):
    stuart = []
    kelwin = []
    # make words
    result = [string[i:j]
              for i in range(len(string)) for j in range(i+1, len(string)+1)]
    ''''res = [test_str[x:y] for x, y in combinations(
    range(len(test_str) + 1), r=2)]
    print(res)

    print(list(combinations(range(len(test_str) + 1), r=2)))''''
    for i in result:
        if(isVowel(i)):
            stuart.append(i)
        else:
            kelwin.append(i)

    return stuart, kelwin


def isVowel(i):
    if len(i) > 0:
        if i[0] == 'A' or i[0] == 'I' or i[0] == 'E' or i[0] == 'O' or i[0] == 'U':
            return True
    else:
        return False
    return False


if __name__ == '__main__':
    s = input()
    s = s.upper()
    stuart, kelwin = minion_game(s)
    print(len(stuart), len(kelwin))
