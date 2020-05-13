"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Input: s = "011101"  /  Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3

Input: s = "00111"  /  Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Input: s = "1111"  /  Output: 3
Constraints:
    2 <= s.length <= 500
    The string s consists of characters '0' and '1' only.
"""

class Solution:
    def maxScore(self, _string):
        count_list = []
        length = len(_string)
        a = b = 0
        for index in range(1, len(_string)):
            first, second = list(_string[:index]), list(_string[index:])
            z_count = first.count('0')
            o_count = second.count('1')
            count_list.append(z_count + o_count)
        return max(count_list)

    def maxScore_method2(self, _string):
        count_list = []
        length = len(_string)
        a = b = 0
        for index in range(1, len(_string)):
            first, second = list(_string[:index]), list(_string[index:])
            a = [a+1 for char in first if char == '0']
            b = [b+1 for char in second if char == '1']
            count_list.append(sum(a)+sum(b))
            a = b = 0
        return max(count_list)

if __name__ == '__main__':
    s = Solution()
    _string ="00111"
    print(s.maxScore(_string))  # 5

    _string = "1111"
    print(s.maxScore(_string))  # 3

    _string = "011101"
    print(s.maxScore(_string))  # 5