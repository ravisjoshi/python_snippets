"""
Count the number of prime numbers less than a non-negative number, n.
Input: 10  /  Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, num):
        if num == 1:
            return 0
        count = 1
        for index in range(3, num+1):
            for num in (2, index//2+1):
                if index % num == 0:
                    break
                count += 1

        return count



if __name__ == '__main__':
    s = Solution()
    num = 10
    print(s.countPrimes(num))
