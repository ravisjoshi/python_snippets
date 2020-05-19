"""
Given two strings s and t , write a function to determine if t is an anagram of s.
Input: s = "anagram", t = "nagaram"  /  Output: true
Input: s = "rat", t = "car"  /  Output: false

Note: You may assume the string contains only lowercase alphabets.
Follow up: What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from random import randint

class Solution:
    def sort_string(self, _str):
        if len(_str) <= 1: return _str

        left, equal, right = [], [], []
        pivot = _str[randint(0, len(_str)-1)]
        for char in _str:
            if char < pivot:    left.append(char)
            elif char == pivot: equal.append(char)
            else:               right.append(char)
        return self.sort_string(left)+equal+self.sort_string(right)

    def isAnagram(self, str1, str2):
        return self.sort_string(str1) == self.sort_string(str2)


if __name__ == '__main__':
    s = Solution()
    str1 = 'anagram'
    str2 = 'nagaram'
    print(s.isAnagram(str1, str2))

