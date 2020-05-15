"""
Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. Determine the minimum number of elements to delete to reach his goal.
For example, if his array is arr = [1, 2, 2, 3] we see that he can delete the 2 elements 1 and 3 leaving. He could also delete both twos and either the 1 or the 3, but that would take 3 deletions. The minimum number of deletions is 2.

Function Description:- Complete the equalizeArray function in the editor below. It must return an integer that denotes the minimum number of deletions required.
equalizeArray has the following parameter(s): arr: an array of integers
Output Format:- Print a single integer that denotes the minimum number of elements Karl must delete for all elements in the array to be equal.

Input: [3, 3, 2, 1, 3]  /  Output: 2
"""

def equalizeArray(arr):
    sorted_array = set(arr)
    num_dict = {}
    for element in sorted_array:
        num_dict.update({element: arr.count(element)})
    return len(arr)-(max([n for n in num_dict.values()]))

if __name__ == '__main__':
    arr = [3, 3, 2, 1, 3]
    print(equalizeArray(arr))
