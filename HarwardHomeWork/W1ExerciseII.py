import math
import random

random.seed(1)
def rand():
    return random.uniform(-1.0,1.0)

#print(rand())
#distance = sqrt((x1-x2)**2 + (y1-y2)**2))
print(math.sqrt(2))

def distance(x, y):
    if len(x) != len(y):
        return "x and y do not have the same length!"
    else:
        square_differences = [(x[i] - y[i])**2 for i in range(len(x))]
        return math.sqrt(sum(square_differences))

def in_circle(x, origin = [0,0]):
    if len(x) != 2:
        return "x is not two-dimensional!"
    elif distance(x, origin) < 1:
        return 1
    else:
        return 0
z = []
def performChecks():
    for i in range(10000):
        x = (rand(),rand())
        z.append(in_circle(x, origin = [0,0]))
    tot = sum(i for i in z if i == 1)
    print(z)
    return tot/10000

print((math.pi/4) - performChecks())

'''
random.seed(1) 

inside = []
R = 10000
for i in range(R):
    point = [rand(), rand()]
    inside.append(in_circle(point))

print(sum(inside) / R)
'''
