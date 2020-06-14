"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Input: arr = [17,18,5,4,6,1]  /  Output: [18,6,6,6,1,-1]
Constraints:
    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
"""

class Solution:
    def replaceElements(self, arr):
        if len(arr) == 1:
            return [-1]
        for index in range(len(arr)-1):
            arr[index] = max(arr[index + 1:])
        arr[-1] = -1
        return arr


s = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(s.replaceElements(arr))

