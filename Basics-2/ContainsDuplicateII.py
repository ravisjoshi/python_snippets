"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Input: nums = [1,2,3,1], k = 3  /  Output: true
Input: nums = [1,0,1,1], k = 1  /  Output: true
Input: nums = [1,2,3,1,2,3], k = 2  /  Output: false
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_dict = {}
        for index, item in enumerate(nums):
            if item in num_dict and index-num_dict[item] <= k:
                return True
            num_dict[item] = index
        return False


if __name__ == '__main__':
    s = Solution()

    nums = [1, 2, 3, 1]
    k = 3
    print(s.containsNearbyDuplicate(nums, k))

    nums = [1, 0, 1, 1]
    k = 1
    print(s.containsNearbyDuplicate(nums, k))

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(s.containsNearbyDuplicate(nums, k))

    nums = [99, 99]
    k = 2
    print(s.containsNearbyDuplicate(nums, k))

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
    k = 3
    print(s.containsNearbyDuplicate(nums, k))

