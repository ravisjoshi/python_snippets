"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Input: "aba"  /  Output: True
Input: "abca"  /  Output: True
Input: "cbbcc"  /  Output: True
Input: "eccer"  /  Output: True
Input: "ebcbbececabbacecbbcbe"  /  Output: True
Explanation: You could delete the character 'c'.

Note: The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution:
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                tmp1 = s[:l] + s[l + 1:]
                tmp2 = s[:r] + s[r + 1:]
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
        return True

