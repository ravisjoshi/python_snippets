"""
Given an integer (signed 32 bits), write a function to check whether there is any quadRoot of this number.
Input: 16  /  Output: true  - 2
Input: 625  /  Output: true - 5
Follow up: Could you solve it without loops/recursion?
"""

class Solution:
    def isQuad(self, num):
        if num == 1:
            return True
        start = mid = preMid= i = 0
        end = num
        while start < end:
            i += 1
            mid = (start + end) // 4
            if preMid == mid:
                for index in range(start, end):
                    if index**4 == num:
                        return True
                return False
            preMid = mid
            if mid ** 4 == num:
                return True
            elif mid ** 4 > num:
                end = mid
            else:
                start = mid
        return False

if __name__ == '__main__':
    s = Solution()
    num = 9
    print(s.isQuad(num))
