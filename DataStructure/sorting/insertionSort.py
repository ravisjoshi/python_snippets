"""
Insertion sort algorithm: https://en.wikipedia.org/wiki/Insertion_sort
"""
from random import randint

def insertion_sort(arr):
    for index in range(1, len(arr)):
        k = arr[index]
        j = index-1
        while arr[j] > k and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
    return arr


# Create random array
def create_array(length=10, max=50):
    arr = []
    for _ in range(length):
        arr.append(randint(0, max))
    return arr


if __name__ == '__main__':
    arr = create_array()

    print('Before sorting: {}'.format(arr))
    print('After sorting:  {}'.format(insertion_sort(arr)))
