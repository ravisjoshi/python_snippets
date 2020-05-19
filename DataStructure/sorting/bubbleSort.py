"""
Bubble Sort: https://en.wikipedia.org/wiki/Bubble_sort
"""
from random import randint

def bubble_sort(arr):
    _len = len(arr)-1
    for index in range(_len):
        for j in range(_len-index):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

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
    print('After sorting:  {}'.format(bubble_sort(arr)))