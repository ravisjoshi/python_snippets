"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Input: "abab"  /  Output: True
Explanation: It's the substring "ab" twice.
Input: "aba"  /  Output: False
Input: "abcabcabcabc"  /  Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

class Solution:
    def repeatedSubstringPattern(self, inputString):
        s_len = len(inputString)
        if s_len == 1:
            return False
        if s_len == 2:
            return inputString[0] == inputString[1]
        sub_str_len = 1
        while sub_str_len <= s_len // 2:
            if s_len % sub_str_len == 0:
                substr = inputString[0:sub_str_len] * (s_len // sub_str_len)
                if substr == inputString:
                    return True
            sub_str_len += 1
        return False

if __name__ == '__main__':
    s = Solution()
    inputString = 'abcaabcaabcaabca'               # abca --> True
    print(s.repeatedSubstringPattern(inputString))

    inputString = 'abcabcabc'                      # abc --> True
    print(s.repeatedSubstringPattern(inputString))

    inputString = 'a'
    print(s.repeatedSubstringPattern(inputString))

    inputString = 'abaababaab'
    print(s.repeatedSubstringPattern(inputString))
