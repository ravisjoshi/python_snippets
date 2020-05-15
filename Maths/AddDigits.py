"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
Input: 38  /  Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    def addDigits(self, num):
        snum = str(num)
        if len(snum) == 1:
            return num
        while len(snum) > 1:
            sum = 0
            for n in snum:
                sum += int(n)
            snum = str(sum)
        return sum


if __name__ == '__main__':
    s = Solution()
    num = 38
    print(s.addDigits(num))

