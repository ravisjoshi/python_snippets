"""
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:

Input: candies = [1,1,2,2,3,3]   /   Output: 3
Explanation: There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.
Input: candies = [1,1,2,3]   /   Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.
Note:
    The length of the given array is in range [2, 10,000], and will be even.
    The number in given array is in range [-100,000, 100,000].
"""
from time import sleep

class Solution:
    def distributeCandiesOneLiner(self, candieList):
        return min(len(candieList) // 2, len(set(candieList)))

    def distributeCandies(self, candieList):
        candies = sorted(candieList)
        c_length = len(candies)
        if len(set(candieList)) <= 3 and c_length // 2 >= len(set(candieList)):
            return len(set(candieList))
        prev_candie = ''
        candie = sisterCount = 0
        while sisterCount <= c_length//2 and candie < c_length:
            if sisterCount == c_length//2:
                return sisterCount
            elif not prev_candie == candies[candie]:
                prev_candie = candies[candie]
                sisterCount += 1
                candie += 1
            else:
                candie += 1
        if prev_candie != candies[-1]:
            sisterCount += 1
        return sisterCount

if __name__ == '__main__':
    s = Solution()
    # candieList = [1, 1, 2, 2, 3, 3]
    # print(s.distributeCandies(candieList))
    # candieList = [1, 1, 1, 1, 3, 3]
    # print(s.distributeCandies(candieList))
    # candieList = [0, 0, 0, 4]
    # print(s.distributeCandies(candieList))
    # candieList = [100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0]
    candieList = [1, 1, 2, 3]
    print(s.distributeCandies(candieList))
