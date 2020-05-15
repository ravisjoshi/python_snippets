"""
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.
Input: n = 4  /  Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
Input: n = 2  /  Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
Input: n = 7  /  Output: "holasss"
Constraints: 1 <= n <= 500
"""

class Solution:
    def generateTheString(self, num):
        a, b, c = 'a', 'b', 'c'
        if num == 1:
            return a
        half = num//2
        if num % 2 == 0:
            return (a*half + b*half) if half % 2 == 1 else (a*(half+1) + b*(half-1))
        if num % 2 == 1:
            return (a*(half+1) + b*(half-1) + c) if half % 2 == 0 else (a*half + b*half + c)

if __name__ == '__main__':
    s = Solution()
    num = 8
    print(s.generateTheString(num))
