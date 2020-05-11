"""
Given an integer, write a function to determine if it is a power of three.
Input: 27  /  Output: true - 3**3
Input: 0  /  Output: false
Input: 9  /  Output: true - 3**2
Input: 45  /  Output: false
Follow up: Could you do it without using any loop / recursion?
"""
from math import log
class Solution:
    def isPowerOfTwo(self, num):
        while num % 2 == 0 and num > 0:
            num //= 2
        return num == 1

    def isPowerOfThree(self, num):
        while num % 3 == 0 and num > 0:
            num //= 3
        return num == 1

    def isPowerOfFour(self, num):
        while num % 4 == 0 and num > 0:
            num //= 4
        return num == 1

if __name__ == '__main__':
    s = Solution()
    num = 27
    print(s.isPowerOfThree(num))

    num = 536870912
    print(s.isPowerOfTwo(num))
