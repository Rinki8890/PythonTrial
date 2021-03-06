from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return self.name,self.score
        
    def comparator(a, b):
        if (b.score > a.score):
            return 1
        elif (b.score == a.score):
            if a.name > b.name:
                print(a.name,b.name,a.name>b.name)
                return 1
            else:
                return -1
        else :
            return -1

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)

#########Logic is #################
'''if a.score > b.score: return -1 
if a.score < b.score: return 1 
if a.name > b.name: return 1 
if a.name < b.name: return -1 
return 0'''
