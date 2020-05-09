"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is `[1, 6, 2, 5, 3, 4].
"""

class Solution:
    def wiggleSorting(self, numList):
        list_length = len(numList)
        if list_length == 1 or list_length == 2:
            return numList


if __name__ == '__main__':
    s = Solution()
    numList = [3, 5, 2, 1, 6, 4]
    print(s.wiggleSorting(numList))

