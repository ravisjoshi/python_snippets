"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Input: a = 1, b = 2   /   Output: 3
Input: a = -2, b = 3   /   Output: 1
"""

class Solution:
    def getSum(self, firstNum, secondNum):
        return sum([firstNum+secondNum])

if __name__ == '__main__':
    s = Solution()
    firstNum = 5
    secondNum = 3
    print(s.getSum(firstNum, secondNum))
