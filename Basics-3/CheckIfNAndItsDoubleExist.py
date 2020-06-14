"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Input: arr = [10,2,5,3]  /  Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Input: arr = [7,1,14,11]  /  Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Input: arr = [3,1,7,11]  /  Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

Constraints:
    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3
"""

class Solution:
    def checkIfExist(self, arr):
        for num in arr:
            if (num*2 in arr and arr.index(num) != arr.index(num*2)) or \
                    (num/2 in arr and arr.index(num) != arr.index(num/2)) or \
                    num == 0 and arr.count(num) >= 2:
                return True
        return False


s = Solution()
arr = [10, 2, 5, 3]
print(s.checkIfExist(arr))

arr = [7, 1, 14, 11]
print(s.checkIfExist(arr))

arr = [3, 1, 7, 11]
print(s.checkIfExist(arr))

arr = [-2, 0, 10, -19, 4, 6, -8]
print(s.checkIfExist(arr))
