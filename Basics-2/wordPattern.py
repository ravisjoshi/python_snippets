"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Input: pattern = "abba", str = "dog cat cat dog"  /  Output: true
Input:pattern = "abba", str = "dog cat cat fish"  /  Output: false
Input: pattern = "aaaa", str = "dog cat cat dog"  /  Output: false
Input: pattern = "abba", str = "dog dog dog dog"  /  Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""

class Solution:
    def wordPattern(self, pattern, _str):

if __name__ == '__main__':
    s = Solution()
    pattern = "abba"
    _str = "dog cat cat dog"
    print(s.wordPattern(pattern, _str))
