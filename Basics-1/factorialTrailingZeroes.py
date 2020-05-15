"""
Given an integer n, return the number of trailing zeroes in n!.
Input: 3  /  Output: 0
Explanation: 3! = 6, no trailing zero.
Input: 5  /  Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroCount = 0
        start = 5
        while start <= n:
            zeroCount += n // start
            start *= 5
        return zeroCount

if __name__ == '__main__':
    s = Solution()
    num = 25
    print(s.trailingZeroes(num))
