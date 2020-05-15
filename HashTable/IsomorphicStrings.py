"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
Input: s = "egg", t = "add"  /  Output: true
Input: s = "foo", t = "bar"  /  Output: false
Input: s = "paper", t = "title"  /  Output: true

Note: You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, str1, str2):
        if not len(str1) == len(str2):
            return False
        if len(set(str1)) != len(set(str2)):
            return False
        iso_dict = {}
        for key, value in zip(str1, str2):
            if key not in iso_dict:
                iso_dict.update({key: value})
            elif value != iso_dict[key]:
                return False
        return True

if __name__ == '__main__':
     s = Solution()
     str1 = "egg"
     str2 = "add"
     print(s.isIsomorphic(str1, str2)) # True

     str1 = "foo"
     str2 = "bar"
     print(s.isIsomorphic(str1, str2))  # False

     str1 = "paper"
     str2 = "title"
     print(s.isIsomorphic(str1, str2))  # True

     str1 = "ab"
     str2 = "aa"
     print(s.isIsomorphic(str1, str2))  # False

