"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Input: [3,0,1]  /  Output: 2
Input: [9,6,4,2,3,5,7,0,1]  /  Output: 8
"""

class Solution:
    def missingNumber(self, nums):
        num = sorted(nums)[0]
        for index in range(-1, len(nums)):
            if not index + 1 in nums:
                return (index + 1)

if __name__ == '__main__':
    s = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(s.missingNumber(nums))
