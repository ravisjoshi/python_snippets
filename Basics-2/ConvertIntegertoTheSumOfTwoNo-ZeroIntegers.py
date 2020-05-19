"""
Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.
Return a list of two integers [A, B] where:
A and B are No-Zero integers.
A + B = n

It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.

Input: n = 2  /  Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.
Input: n = 11  /  Output: [2,9]
Input: n = 10000  /  Output: [1,9999]
Input: n = 69  /  Output: [1,68]
Input: n = 1010  /  Output: [11,999]
Constraints: 2 <= n <= 10^4
"""

class Solution:
    def getNoZeroIntegers(self, num):
        result = []
        for index  in range(1, num//2):
            if '0' not in str(index) and '0' not in str(num-index):
                result.append(index)
                result.append(num-index)
                break
        return result

if __name__ == '__main__':
    s = Solution()
    num = 11
    print(s.getNoZeroIntegers(num))
