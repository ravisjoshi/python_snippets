"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Input: 28  /  Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)
"""

from time import time
from math import sqrt


class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        s_list = []
        for index in range(1, int(sqrt(num))+1):
            if num % index == 0:
                if index not in s_list: s_list.append(index)
                if num//index not in s_list and num//index != num:
                    s_list.append(num//index)
        return True if sum(s_list) == num else False


s = Solution()

num = -6
print(s.checkPerfectNumber(num))

num = 6
print(s.checkPerfectNumber(num))

start = time()
num = 99999992
print(s.checkPerfectNumber(num))
end = time()
print('Time taken: {}'.format(end - start))






