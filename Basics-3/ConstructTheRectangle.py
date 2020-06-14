"""
For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.

Input: 4  /  Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

Note:
    The given area won't exceed 10,000,000 and is a positive integer
    The web page's width and length you designed must be positive integers.
"""
import sys
from itertools import combinations, permutations
from math import sqrt

class Solution:
    def constructRectangle(self, area):
        for index in range(int(sqrt(area)), 0,-1):
            if area % index == 0:
                return [area//index, index]

    def constructRectangle_BruteForce(self, area):
        if area == 1:
            return [1, 1]
        factors = [area]
        for index in range(1, area//2+1):
            if area % index == 0:
                factors.append(index)
        factors.append(int(sqrt(area)))

        output = {}
        for l, w in permutations(factors, 2):
            if l*w == area and l >= w:
                output.update({l: w})

        min_value, result = sys.maxsize, [0, 0]
        for l, w in output.items():
            if (l - w) < min_value:
                result[0] = l
                result[1] = w
                min_value = l - w

        return result

s = Solution()

area = 10
print(s.constructRectangle(area))

area = 4
print(s.constructRectangle(area))

area = 9
print(s.constructRectangle(area))

