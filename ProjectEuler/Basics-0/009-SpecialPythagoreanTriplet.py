"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagoreanTriplet(num):
    for a in range(1, num//2):
        for b in range(a+1, num//2):
            c = num - (a+b)
            if (a*a + b*b == c*c):
                print('Values:- a={} b={} c={}'.format(a, b, c))
                return a*b*c

num = 1000
print(pythagoreanTriplet(num))
