"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
---
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution:
    def reverseString(self, inputString):
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(inputString)-1
        for index in range(length//2+1):
            temp = inputString[index]
            inputString[index] = inputString[length-index]
            inputString[length - index] = temp

        print(inputString)

if __name__ == '__main__':
    s = Solution()
    inputString = ["h", "e", "l", "l", "o"]
    s.reverseString(inputString)
