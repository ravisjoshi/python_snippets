"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
Input: "Hello"  /  Output: "hello"
Input: "here"  /  Output: "here"
Input: "LOVELY"  /  Output: "lovely"
"""

class Solution:
    def toLowerCase(self, inputString):
        return "".join([chr(ord(char)+32) if ord('A') <= ord(char) <= ord('Z') else char for char in inputString])

    def toLowerCase_method2(self, inputString):
        newList = []
        for char in inputString:
            if ord('A') <= ord(char) <= ord('Z'):
                newList.append(chr(ord(char)+32))
            else:
                newList.append(char)
        return "".join(newList)


if __name__ == '__main__':
    s = Solution()
    inputString = 'Hello'
    print(s.toLowerCase(inputString))

    inputString = 'LOVELY'
    print(s.toLowerCase_method2(inputString))
