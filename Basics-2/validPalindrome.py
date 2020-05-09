"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Input: "A man, a plan, a canal: Panama"  /  Output: true
Input: "race a car"  /  Output: false
"""
import re

class Solution:
    def isPalindrome(self, testString):
        newString = re.sub('[^A-Za-z0-9]+', '', testString).lower()
        startIndex = 0
        endIndex = len(newString)-1
        while startIndex <= endIndex:
            if not newString[startIndex] == newString[endIndex]:
                return False
            startIndex += 1
            endIndex -= 1
        return True

if __name__ =='__main__':
    s = Solution()
    testString = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(testString))
    testString = "0P"
    print(s.isPalindrome(testString))