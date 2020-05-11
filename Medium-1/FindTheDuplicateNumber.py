"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
Input: [1,3,4,2,2]  /  Output: 2
Input: [3,1,3,4,2]  /  Output: 3
Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution:
    def findDuplicate(self, nums):
        sortedDict = {}
        for index, number in enumerate(nums):
            if number not in sortedDict.keys():
                sortedDict.update({number: index})
            else:
                return number

    def findDuplicate_method2(self, nums):
        sortedList = sorted(nums)
        prevNum = 0
        for num in sortedList:
            if num == prevNum:
                return num
            else:
                prevNum = num

if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 4, 2, 2]
    print(s.findDuplicate(nums))
