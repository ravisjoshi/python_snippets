"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Input: [1,2,3]  /  Output: [1,2,4]
Explanation: The array represents the integer 123.
Input: [4,3,2,1]  /  Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plusOne(self, digits):
        remainder = 0
        for i in range(len(digits)-1, -1, -1):
            temp = digits[i]+1
            if temp < 10:
                digits[i] = temp
                remainder = 0
                break
            else:
                digits[i] = 0
                remainder = 1
        if remainder == 1:
            digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    s = Solution()
    # digitsList = [1, 2, 3]
    # digitsList = [4, 3, 2, 1]
    # digitsList = [0]
    digitsList = [9, 9, 9]
    print(s.plusOne(digitsList))
