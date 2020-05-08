"""
Given a 32-bit signed integer, reverse digits of an integer.
Input: 123  /  Output: 321
Input: -123  /  Output: -321
Input: 120  /  Output: 21
"""
class Solution:
    def reverse(self, num):
        if num >= 2 ** 31 - 1 or num <= -2 ** 31:
            return 0
        result = 0
        flag = 1 if num > 0 else -1
        num = num if num > 0 else num*flag

        position = len(str(num))
        while num > 0:
            position -= 1
            remainder = num % 10
            num = num // 10
            result += remainder * 10**position

        return 0 if result >= 2 ** 31 - 1 or result <= -2 ** 31 else result*flag

if __name__ == '__main__':
    s = Solution()
    num = 1534236469
    print(s.reverse(num))
