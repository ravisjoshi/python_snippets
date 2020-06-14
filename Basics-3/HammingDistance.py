"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.

Input: x = 1, y = 4
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""

from itertools import zip_longest
class Solution:
    def hammingDistance(self, x, y):
        diff = x ^ y
        count = 0
        while diff:
            if diff & 1 == 1:
                count += 1
            diff = diff >> 1
        return count

    def hammingDistance_somethingRandom(self, x, y):
        bx = bin(x)[2:]
        by = bin(y)[2:]
        if len(bx) > len(by):
            by = '0'*(len(bx)-len(by)) + by
        elif len(by) > len(bx):
            bx = '0'*(len(by)-len(bx)) + bx
        index = 0
        for i, j in zip_longest(list(bx), list(by)):
            if i !=j: index += 1
        return index


s = Solution()
x = 4; y = 14
print(s.hammingDistance(x, y))