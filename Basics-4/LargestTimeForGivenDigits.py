"""
Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Input: [1,2,3,4]  /  Output: "23:41"
Input: [5,5,5,5]  /  Output: ""

Note:
    A.length == 4
    0 <= A[i] <= 9
"""

from itertools import permutations


class Solution:

    def largestTimeFromDigits(self, A):
        A = map(str, A)
        _max_time = {}
        for c in permutations(A):
            h, m = c[0] + c[1], c[2] + c[3]
            if 0 <= int(h) < 24 and 0 <= int(m) < 59:
                if h not in _max_time:
                    _max_time.update({h: m})
                elif int(m) > int(_max_time[h]):
                    _max_time.update({h: m})

        return max(_max_time) + ":" + _max_time[max(_max_time)] if _max_time else ""


s = Solution()

A = [1, 1, 0, 1]
print(s.largestTimeFromDigits(A))

A = [1, 2, 3, 4]
print(s.largestTimeFromDigits(A))

A = [0, 0, 0, 0]
print(s.largestTimeFromDigits(A))

A = [5, 5, 5, 5]
print(s.largestTimeFromDigits(A))

