"""
Heap sort: https://en.wikipedia.org/wiki/Heapsort
"""
from random import randint


def create_array(length=10, max=50):
    arr = []
    for _ in range(length):
        arr.append(randint(0, max))
    return arr


print(create_array())

