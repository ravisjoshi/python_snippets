"""
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Input: 6  /  Output: true
Explanation: 6 = 2 × 3
Input: 8  /  Output: true
Explanation: 8 = 2 × 2 × 2
Input: 14  /  Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:
    1 is typically treated as an ugly number.
    Input is within the 32-bit signed integer range: [−231,  231 − 1].
"""

class Solution:
    def isUgly(self, num):
        while num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            if num % 2 == 0:
                num //= 2
            if num % 3 == 0:
                num //= 3
            if num % 5 == 0:
                num //= 5
        return num == 1

if __name__ == '__main__':
    s = Solution()
    num = 10
    print(s.isUgly(num))
