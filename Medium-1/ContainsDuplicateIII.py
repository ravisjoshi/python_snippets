"""
Given an array of integers, find out whether there are two distinct indices i and j in the array
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference
between i and j is at most k.

Input: nums = [1,2,3,1], k = 3, t = 0  /  Output: true
Input: nums = [1,0,1,1], k = 1, t = 2  /  Output: true
Input: nums = [1,5,9,1,5,9], k = 2, t = 3  /  Output: false
"""
import itertools

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):



if __name__ == '__main__':
    s = Solution()

    nums = [1, 2, 3, 1]; k = 3; t = 0
    print(s.containsNearbyAlmostDuplicate(nums, k, t))

    nums = [1, 0, 1, 1]; k = 1; t = 2
    print(s.containsNearbyAlmostDuplicate(nums, k, t))

    nums = [1, 5, 9, 1, 5, 9]; k = 2; t = 3
    print(s.containsNearbyAlmostDuplicate(nums, k, t))

