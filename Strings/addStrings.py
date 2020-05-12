"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1, num2):
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        num2 = num2.zfill(len(num1))
        remainder = 0
        _sum = ''
        for n1, n2 in zip(num1[::-1], num2[::-1]):
            temp = int(n1) + int(n2) + remainder
            remainder = 0
            if temp > 9:
                remainder = temp // 10
            _sum += str(temp % 10)
        if remainder != 0:
            _sum += str(remainder)

        return _sum[::-1]

if __name__ == '__main__':
    s =Solution()
    num1 = '408'
    num2 = '5'
    print(s.addStrings(num1, num2))

