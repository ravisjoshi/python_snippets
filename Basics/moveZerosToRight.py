"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Input: [0,1,0,3,12]  /  Output: [1,3,12,0,0]
Input: [1,0,1]  /  Output: [1,1,0]
Input: nums = [1, 0, 0, 1, 5, 8, 2]  /  Output: [1, 1, 5, 8, 2, 0, 0]
"""

class Solution:
    def moveZeroes(self, nums):
        if len(nums) > 1:
            length = len(nums)
            for index in range(length):
                if nums[index] == 0:
                    for j in range(index+1, length):
                        if nums[j] != 0:
                            nums[index] = nums[j]
                            nums[j] = 0
                            break
        return nums

if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    print(s.moveZeroes(nums))
