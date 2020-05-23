
from time import time

## Generator method
start_time = time()
num =100000000
my_gen = (n*n for n in range(1, num))
for n in my_gen:
    print(n, end=', ')
end_time = time()
print('Elapsed time: {}'.format(end_time - start_time))
time_taken_by_generator = end_time - start_time


## List method
start_time = time()
num =100000000
my_sq = [n*n for n in range(1, num)]
print(my_sq)
end_time = time()
print('Elapsed time: {}'.format(end_time - start_time))
time_taken_by_list = end_time - start_time

print('Generator took: {}'.format(time_taken_by_generator))
print('List took:      {}'.format(time_taken_by_list))
