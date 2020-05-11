"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
Input: n = 4  /  Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Input: n = 25  /  Output: 1389537
Constraints: 0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

class Solution:
    def tribonacci(self, num):
        if num == 0:
            return 0
        elif num == 1 or num == 2:
            return 1
        first, second, third = 0, 1, 1
        tribo_list = [first, second, third]
        for number in range(3, num):
            tribo = third + second + first
            tribo_list.append(tribo)
            first, second, third = second, third, tribo
        return (tribo_list[-1] + tribo_list[-2] + tribo_list[-3])

if __name__ == '__main__':
    s =Solution()
    num = 5
    print(s.tribonacci(num))
