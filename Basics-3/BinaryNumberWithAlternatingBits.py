"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Input: 5  /  Output: True
Explanation: The binary representation of 5 is: 101

Input: 7  /  Output: False
Explanation: The binary representation of 7 is: 111.

Input: 11  /  Output: False
Explanation: The binary representation of 11 is: 1011.

Input: 10  /  Output: True
Explanation: The binary representation of 10 is: 1010.
"""

class Solution:
    def hasAlternatingBits(self, num):
        if num == 1:
            return True
        s_bin = bin(num)[2:]
        print(s_bin)
        l_num = len(s_bin)

        for index in range(1, l_num):
            if s_bin[index-1] == s_bin[index]:
                return False
        return True


s = Solution()

for i in range(1, 100):
    num = i
    print(s.hasAlternatingBits(num))
    print(25*'-')

# num = 1
# print(s.hasAlternatingBits(num))


