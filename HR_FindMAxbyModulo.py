'''You are given a function . You are also given  lists. The  list consists of  elements.
You have to pick one element from each list so that the value from the equation below is maximized:
denotes the element picked from the  list . Find the maximized value  obtained.
denotes the modulo operator.
Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
'''
from itertools import product

def findMax():
    n = input("no of lists and modulo \n").split()
    nooflists = int(n[0])
    modulo = int(n[1])
    maxbymodulo = []
    final = 0

    for i in range(nooflists):
        a_i = list(map(int,input().split()))
        l_i = product(*a_i)
        #l_i = [int(i)**2 for i in a_i]
        maxbymodulo.append(list(l_i))
    print(maxbymodulo)

findMax()

##This one is wrong