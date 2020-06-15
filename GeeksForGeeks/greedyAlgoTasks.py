'''T = int(input())
N = int(input())
start = list(map(int, input().split()))
finish = list(map(int, input().split()))'''
start = [1, 3, 2, 5,4]
finish = [2, 4, 3,6,5]
c = 0
result = []
idx = finish.index(min(finish))
for i in range(len(start)):
    if(i>1):
        if min(finish) <= start[idx+1]:
            result.append(min(finish))
            idx = finish.index(min(finish))
            finish.remove(min(finish))
            start.pop(idx)
        else:
            finish.pop(idx+1)
            start.pop(idx+1)
for i in range(len(start)):
    idx = finish.index(min(finish))
    if max(result) <= start[idx]:
            result.append(min(finish))
            idx = finish.index(min(finish))
            finish.remove(min(finish))
            start.pop(idx)
    else:
        if(len(start)>0):
            finish.pop(idx)
            start.pop(idx)
print(result)
print(start)
print(finish)
