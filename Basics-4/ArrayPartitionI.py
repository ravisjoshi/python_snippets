"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Input: [1,4,3,2]  /  Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Input: [7,3,1,0,0,6]  / Output: 7

Note:
    n is a positive integer, which is in the range of [1, 10000].
    All the integers in the array will be in the range of [-10000, 10000].
"""

class Solution:

    def arrayPairSum_quickOne(self, nums):
        nums.sort()
        return (sum(nums[::2]))

    def arrayPairSum(self, nums):
        if len(nums) == 2:
            return min(nums)
        nums = sorted(nums)
        _sum = 0
        start = 0
        end = len(nums) - 1
        while start < end:
            _sum += min(nums[start], nums[start + 1])
            start += 2
            if start + 2 < end:
                _sum += min(nums[end], nums[end - 1])
                end -= 2

        return _sum

    def arrayPairSum_another_approach(self, nums):
        nums = sorted(nums)
        length = len(nums)
        _sum = 0
        for index in range(0, length, 2):
            _sum += nums[index]

        return _sum



s = Solution()

nums = [7, 3, 1, 0, 0, 6]
print(s.arrayPairSum_quickOne(nums))

nums = [1, 1]
print(s.arrayPairSum_quickOne(nums))

nums = [1, 4, 3, 2]
print(s.arrayPairSum_quickOne(nums))
