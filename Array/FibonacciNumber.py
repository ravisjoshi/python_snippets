"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
Input: 2  /  Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Input: 3  /  Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Input: 4  /  Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
Note: 0 ≤ N ≤ 30.
"""

class Solution:
    def fib(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        first, second = 0, 1
        final = [first, second]
        for _ in range(2, number):
            third = first + second
            final.append(third)
            first, second = second, third
        return (final[-1] + final[-2])

if __name__ == '__main__':
    s = Solution()
    num = 4
    print(s.fib(num))

