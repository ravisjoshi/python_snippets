"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note: Assume the length of given string will not exceed 1,010.
Input: "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution:
    def longestPalindrome(self, inputString):
        if inputString == "":
            return 0
        elif len(inputString) == 1:
            return 1
        finalCount = mid = 0
        singleChars = set(inputString)
        for char in singleChars:
            if inputString.count(char) % 2 == 0:
                finalCount += inputString.count(char)
            elif (inputString.count(char) -1) % 2 == 0:
                mid = 1
                finalCount += inputString.count(char)-1
        finalCount += mid
        return finalCount

if __name__ == '__main__':
    s = Solution()
    inputString = 'abccccdd'
    print(s.longestPalindrome(inputString))


