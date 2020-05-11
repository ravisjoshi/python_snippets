"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.
Input: "Hello World"  /  Output: 5
Input: ""  /  Output: 0
Input: " "  /  Output: 0
Input: "Hello  "  /  Output: 5
"""

class Solution:
    def lengthOfLastWord(self, inputString):
        if inputString == "":
            return 0
        elif not inputString.isspace() and list(inputString.split())[-1].isalpha():
            return len(list(inputString.split())[-1])
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    inputString = "Hello World"
    # inputString = ""
    # inputString = " "
    # inputString = "Hello  "
    # inputString = "   World"
    # print(s.countAndSay(num))
    print(s.lengthOfLastWord(inputString))
