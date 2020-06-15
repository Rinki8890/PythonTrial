circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results = list(zip(my_strings, my_numbers))

print(results)

from functools import reduce 

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: x+2, my_floats))
filter_result = list(filter(lambda name: name==name[::-1], my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 10)

print(map_result)
print(filter_result)
print(reduce_result)

# Python 3
from functools import reduce
#reduce(func, iterable[, initial])
numbers = [3, 4, 6, 9, 34, 12]
#The result, as you'll expect, is 78 because reduce, initially, uses 10 as the first argument to custom_sum.
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers, 10)
print(result)

a = map(int,input().split())
b = map(int,input().split())

from itertools import product
print(*list(product(a,b)))