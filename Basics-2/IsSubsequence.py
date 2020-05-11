"""
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
s = "abc", t = "ahbgdc"   /   Return true.
s = "axc", t = "ahbgdc"   /   Return false.
s = "acb", t = "ahbgdc"   /   Return false.
Follow up: If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""

class Solution:
    def isSubsequence(self, firstString, secondString):
        j = 0
        cnt = len(firstString)
        if not firstString:
            return True
        for char in secondString:
            if char == firstString[j]:
                j += 1
            if j == cnt:
                return True
        return False

    def isSubsequenceMethod1(self, firstString, secondString):
        if firstString == "":
            return True
        elif secondString == "":
            return False
        _fCount = _sCount = 0
        flag = False
        while _fCount < len(firstString) and _sCount < len(secondString):
            if not firstString[_fCount] == secondString[_sCount]:
                flag = False
                _sCount += 1
            else:
                _fCount += 1
                _sCount += 1
        if firstString[-1] == secondString[_sCount-1] and _fCount == len(firstString):
            return True
        return flag


if __name__ == '__main__':
    s = Solution()
    firstString = "axc"
    secondString = "ahbgdc"

    print(s.isSubsequence(firstString, secondString))

