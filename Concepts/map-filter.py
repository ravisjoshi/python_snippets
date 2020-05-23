## map syntax
# map(function, iterable_data)
# Example - 1

import math
radii = [1, 2, 3, 4, 5, 6, 7]
area = lambda r: math.pi * (r**2)
print(list(map(area, radii)))

# Example - 2
_list = ['1', '2', '3', '4', '5']
for i in map(int, _list):
    print(i*i)
# 1 4 9 16 25

# Example - 3
num_list = ['1', '2', '3', '4', '5']
sq_list = [n*n for n in map(int, num_list)]
print(sq_list)

# Example - 4
num_list = [1, 2, 3, 4, 5]
sq = lambda n: n*n
print(list(map(sq, num_list)))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## filter syntax
# filter(function, iterable_data) - used to select certain pieces of data from a list, tuple or other collection of data.
# Example - 1

import statistics
data = [1, 2, 3, 4, 5, 6]
avg = statistics.mean(data)
print(list(filter(lambda data: data > avg, data)))

# Example - 2
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, num_list)))

