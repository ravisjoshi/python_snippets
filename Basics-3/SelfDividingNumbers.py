"""
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Input: left = 1, right = 22  /  Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note: The boundaries of each input argument are 1 <= left <= right <= 10000
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        result = []
        for index in range(left, right+1):
            temp = []
            num = index
            if '0' not in str(index):
                while num > 0:
                    if not index % (num % 10) == 0:
                        temp.append(False)
                        break
                    else:
                        temp.append(True)
                        num //= 10
                if all(temp): result.append(index)

        return result


s = Solution()
left = 1; right = 22
print(s.selfDividingNumbers(left, right))

left = 1; right = 10000
print(s.selfDividingNumbers(left, right))




