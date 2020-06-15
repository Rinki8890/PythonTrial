def minion_game(s):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")
    '''result = [string[i:j]
              for i in range(len(string)) for j in range(i+1, len(string)+1)]
    res = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r=2)]'''

if __name__ == '__main__':
    s = input()
    minion_game(s)

#If each substring is given 1 point then it is as good as length of a substring from a point.
#ABC >> A, AB, ABC -- 3 substrings is as good as len(ABC) which is 3
#max no of substring we can gain is the length of that substring.