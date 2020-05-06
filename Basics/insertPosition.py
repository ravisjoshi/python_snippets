"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Input: [1,3,5,6], 5  /  Output: 2
Input: [1,3,5,6], 2  /  Output: 1
Input: [1,3,5,6], 7  /  Output: 4
Input: [1,3,5,6], 0  /  Output: 0
"""

class Solution:
    def searchInsert(self, nums, target):
        if nums == []:
            return 0
        elif target in nums:
            return nums.index(target)
        else:
            position = 0
            for num in nums:
                if num < target:
                    position += 1
            return position

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,5,6]
    target = 0
    print(s.searchInsert(nums, target))
