"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
# Too bad, but came up with this one for now...

import time

def nthPrimeNumber(_count):
    k, num = 2, 3
    while k < _count:
        flag = 0
        num += 1
        for index in range(2, num//2+1):
            if num % index == 0:
                flag = 0
                break
            else: flag = 1
        if flag == 1:
            k += 1
            # print('num:{}  k: {}'.format(num, k))
    return num

_count = 10001
start = time.time()
print(nthPrimeNumber(_count))
end = time.time()
print('Time elapsed: {}'.format(end-start))
