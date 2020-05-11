"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
Input: [3, 2, 1]  /  Output: 1
Input: [1, 2]  /  Output: 2
Input: [2, 2, 3, 1]  /  Output: 1
Both numbers with value 2 are both considered as second maximum.
"""

class Solution:
    def thirdMax(self, nums):
        newList = sorted(list(set(nums)))
        if len(newList) < 3:
            return max(nums)
        return newList[-3]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 3, 1]
    print(s.thirdMax(nums))
