import random
random.seed(1)
def moving_window_average(x, n_neighbors=1):
    n = len(x) #lenght of previous list
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    mean = []
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    for i in range(0,n):
        #print(x[i:i+width])
        mean.append(sum(x[i:i+width])/width)
    return mean
    ## return [sum(x[i:(i+width)]) / width for i in range(n)]
x = [random.random() for _ in range(1000)]
#print(x)
print(x[8:11])
print(x[10]/5)
Y_ = [moving_window_average(x, i) for i in range(0,10)]
Y = [sum(moving_window_average(x, i)) for i in range(0,10)]
#print(Y_)

ranges = [max(x) - min(x) for x in Y_]
#print(ranges)