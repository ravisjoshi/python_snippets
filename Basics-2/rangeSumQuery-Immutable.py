"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.
"""

class NumArray:

    def __init__(self, nums):
        self.numList = nums

    def sumRange(self, i, j):
        sum = 0
        for index in range(i, j+1):
            sum += self.numList[index]
        return sum

if __name__ == '__main__':
    numList = [-2, 0, 3, -5, 2, -1]
    s = NumArray(numList)
    startIndex = 0
    endIndex = 5
    print(s.sumRange(startIndex, endIndex))
