"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
Note:
    All letters in hexadecimal (a-f) must be in lowercase.
    The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
    The given number is guaranteed to fit within the range of a 32-bit signed integer.
    You must not use any method provided by the library which converts/formats the number to hex directly.
Input: 26  /  Output: "1a"
Input: -1  /  Output: "ffffffff"
"""

class Solution:
    def toHex(self, num):
        if not num:
            return '0'
        output, remainder = '', 0
        hexDict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num > 0:
            while num:
                output += hexDict[num % 16]
                num //= 16
        elif num < 0:
            n = num + 2 ** 32
            while n:
                output += hexDict[n % 16]
                n //= 16
        return output[::-1]

if __name__ == '__main__':
    s = Solution()
    num = -2
    print(s.toHex(num))
