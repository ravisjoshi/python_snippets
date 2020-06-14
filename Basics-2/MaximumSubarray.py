"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4]  /  Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return sum(nums)
        max_sum, temp = 0, 0
        for num in nums:
            temp += num
            max_sum = max(max_sum, temp)
            if temp < 0:
                temp = 0
        return max_sum if max_sum > 0 else max(nums)


s = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))
