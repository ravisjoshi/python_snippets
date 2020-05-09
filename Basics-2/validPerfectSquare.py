"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.
Input: 16  /  Output: true
Input: 14  /  Output: false
"""

class Solution:
    def isPerfectSquare(self, num):
        if num == 0 or num == 1:
            return True
        low = 0
        high = num
        for _ in range(64):
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid
            else:
                low = mid

        return False

if __name__ == '__main__':
    s = Solution()
    num = 14
    print(s.isPerfectSquare(num))