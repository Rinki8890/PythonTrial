from bisect import bisect
n = int(input())
scores = list(set(map(int, input().split())))
l = len(scores)
scores.sort()
m = int(input())
alice = map(int, input().split())
for i in alice:
    print (l - bisect(scores, i) + 1)

##########Time inefficient
def climbingLeaderboard(scores, alice):
    res = []
    s = sorted(set(scores),reverse = True)
    print(s)
    if len(alice) == 0:
        return 0 
    for a in alice:   
        if a in s:
            res.append(s.index(a)+1)
        else:
            s = sorted(set(scores+[a]),reverse = True)
            res.append(s.index(a)+1)
        s.remove(a)
    return res