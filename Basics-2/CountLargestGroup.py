"""
NOTE: The question is simply asking you for the highest frequency of the nums.
    For example 13 (Whos sum is 1 + 3 = 4) and a range from 1 to 13 will have the number 4 occurring twice.
    Essentially the count of number(s) with the highest frequency should be returned.

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.
Return how many groups have the largest size.

Input: n = 13  /  Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Input: n = 2  /  Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Input: n = 15  /  Output: 6
Input: n = 24  /  Output: 5

Constraints: 1 <= n <= 10^4


"""

import collections

class Solution:
    def countLargestGroup(self, n):
        res = []
        for i in range(1, n + 1):
            res.append(sum(int(x) for x in str(i)))

        c = collections.Counter(res)
        x = [i for i in c.values() if i == max(c.values())]
        return len(x)


s = Solution()

num = 13
print(s.countLargestGroup(num))

num = 15
print(s.countLargestGroup(num))

num = 24
print(s.countLargestGroup(num))

