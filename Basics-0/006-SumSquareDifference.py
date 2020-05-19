"""
The sum of the squares of the first ten natural numbers is, 12+22+...+102=385
The square of the sum of the first ten natural numbers is, (1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumSquareDiff(num):
    """
    Method-1:-
    squareSum = num*(num+1)*((2*num)+1)//6
    sumSquare = (num*(num+1)//2)**2
    print(sumSquare - squareSum)

    Method-2:-
    print(((num*(num+1))//2)**2 - sum([n**2 for n in range(1, num+1)]))

    But we will do below one:--
    """

    _square_sum = 0
    _sum_square = 0
    for index in range(1, num+1):
        _square_sum += index**2
        _sum_square += index

    return _sum_square**2 - _square_sum

num = 100
print(sumSquareDiff(num))
