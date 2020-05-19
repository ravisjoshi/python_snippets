"""
Quick Sort: https://en.wikipedia.org/wiki/Quicksort
Ref:
https://www.youtube.com/watch?v=1Mx5pEeTp3A
https://www.youtube.com/watch?v=RFyLsF9y83c
"""

from random import randint

def quick_sort(arr):
    if len(arr) <= 1: return arr

    left, equal, right = [], [], []
    pivot = arr[randint(0, len(arr)-1)]

    for element in arr:
        if element < pivot:    left.append(element)
        elif element == pivot: equal.append(element)
        else:                  right.append(element)
    return quick_sort(left)+equal+quick_sort(right)

# Create random array
def create_array(length=10, max=50):
    arr = []
    for _ in range(length):
        arr.append(randint(0, max))
    return arr

if __name__ == '__main__':

    arr = create_array()
    print('Before sorting: {}'.format(arr))
    print('After sorting:  {}'.format(quick_sort(arr)))
