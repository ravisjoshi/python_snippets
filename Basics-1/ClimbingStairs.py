"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
Input: 2  /  Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Input: 3  /  Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, num):
        if num == 1 or num == 2:
            return num
        no_of_ways = 0
        first, second = 1, 2

        for _ in range(2, num):
            no_of_ways = first + second
            first, second = second, no_of_ways

        return no_of_ways


    def climbStairs_method2(self, num):
        if num == 1 or num == 2:
            return num
        no_of_ways = self.climbStairs(num-1) + self.climbStairs(num-2)
        return no_of_ways


if __name__ == '__main__':
    s = Solution()
    num = 7
    print(s.climbStairs_method2(num))
