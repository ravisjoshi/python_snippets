"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def largestPrimeNumber(num):
    divisor = 1
    index = 2
    while num > 1:
        if num % index == 0:
            print('{} did divide {}'.format(index, num))
            divisor = index
            num //= index
        index += 1
    return divisor

num = 600851475143
print(largestPrimeNumber(num))
