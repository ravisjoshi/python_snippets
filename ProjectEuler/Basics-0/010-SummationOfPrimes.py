"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from time import time
from math import sqrt

"""
Sieve of Eratosthenes
"""
def sieveOfEratosthenes(num):
    _lst = list(range(num))
    for index in range(2, int(sqrt(num))):
        if _lst[index] != 0:
            for j in range(index*index, num, index):
                _lst[j] = 0
    return _lst


num = 2000000
start = time()
print(sum(sorted(set(sieveOfEratosthenes(num)))[2:]))
end = time()
print('Time elapsed: {}'.format(end-start))


"""
Brute force method
"""
def sumOfPrimes(num):
    result = [2, 3]
    _sum = 5
    for n in range(4, num):
        flag = 1
        for index in range(2, int(sqrt(n))+1):
            if n % index == 0:
                flag = 0
                break
        if flag == 1:
            result.append(n)
    return sum(result)

num = 2000000
start = time()
print(sumOfPrimes(num))
end = time()
print('Time elapsed: {}'.format(end-start))
