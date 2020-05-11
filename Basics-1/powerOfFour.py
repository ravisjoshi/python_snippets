"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Input: 16  /  Output: true
Input: 5  /  Output: false
Follow up: Could you solve it without loops/recursion?
"""
from math import log

class Solution:
    def isPowerOfFour(self, num):
        return log(num, 4).is_integer()

if __name__ == '__main__':
    s = Solution()
    num = 9
    print(s.isPowerOfFour(num))
