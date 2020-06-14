"""
Given two integer arrays of equal length target and arr.
In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.
Return True if you can make arr equal to target, or False otherwise.

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.

Input: target = [7], arr = [7]  /  Output: true
Explanation: arr is equal to target without any reverses.

Input: target = [1,12], arr = [12,1]  /  Output: true
Input: target = [3,7,9], arr = [3,7,11]  /  Output: false
Explanation: arr doesn't have value 9 and it can never be converted to target.

Input: target = [1,1,1,1,1], arr = [1,1,1,1,1]  /  Output: true

Constraints:
    target.length == arr.length
    1 <= target.length <= 1000
    1 <= target[i] <= 1000
    1 <= arr[i] <= 1000
"""

class Solution:
    def canBeEqual(self, target, arr):
        return True if sorted(target) == sorted(arr) else False


s = Solution()

target = [1, 2, 3, 1, 4]
arr = [2, 1, 4, 1, 3]
print(s.canBeEqual(target, arr))


target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(s.canBeEqual(target, arr))

target = [937, 396, 309, 316, 278, 305, 937, 563, 385, 816, 333, 523, 874, 47, 281, 984, 431, 692]
arr = [937, 385, 816, 937, 309, 523, 281, 278, 316, 396, 984, 431, 47, 333, 692, 874, 563, 305]
print(s.canBeEqual(target, arr))
