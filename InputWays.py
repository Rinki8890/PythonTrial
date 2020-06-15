#Many strings in one line, input
*a,b = input().strip()
import sys
#inputs are Hack 2 and all should be given in one line
#since strip will treat it as a string and there will be so many strings, *is placed for the firat value

a = input().split()
#anything can be given as a list, hack 2 3 4 5 but all should be given in one line
li=[]
for line in sys.stdline():
    li.append(line)
    #if line contains lot of entries in one line hence need to make a list.
    # if inputs are in separate line then line will take them one by one, line by line

a = map(int,input().split())
#maps all the input of a single line to int and returns a map object which can be converted to a list.

b, c = map(int, input().split())
print (str(b+c) + " " + s)

o,d = input().split()
#input a 5 o/p : a 5

orders = []
for _ in range(n):
        orders.append(map(int, input().rstrip().split()))
#input is:
'''8 1
4 2
5 6
3 1
4 3'''

#A list in an input
li = list(map(int,input().split()))
#input is a list, eg 2 3 4

li = (list(map(int,input().split())) for _ in range(a))
#input is many lists
# for eg 2 3 4
# 1 2 3 (within range of a)

S = Counter(map(int,input().split()))
#directly changing a list to dictionary

print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
#*map(int,input().split() this line is as good as line number 1.
#mapping the input and sice it has not been assigned to the variables(input is more than one)
#a star has beeen amrked so that it is considered as more than one input

l = list(s.strip())
#chanign string input s to a list

inp = list(map(int,input().strip()))
#input was 67868686 and got converted to [6,7,8,6,8,6,8,6]

#groups = accumulate(arr) : i/p : 3 7 4 6 5, o/p: 3, 10, 14, 20, 25

# reverse loop
for i in range(len(a)-1, -1, -1):
        pass
for i in reversed(range(len(a)-1)):
        pass

#Converting a string into list
s = list(s)

#use zip to convert anything into tuple:
list(zip(*indices of a 2d array)) #returns list of tuples(indices)
#list(zip(*np.where(board == 0))) np.where will returns list of indices satisfying the condition

 n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
#input will be 
"""3
1 3
2 3
3 3"""

##printing findings:

servtime = [([1, 3], 4), ([2, 3], 5), ([3, 3], 6)]

#servtime[0] >  ([1, 3], 4)
#servtime[0][0] > [1,3]
#servtime[0][1] > 4
#servtime[0][0][0] > 1
#servtime[0][0][1] > 3


