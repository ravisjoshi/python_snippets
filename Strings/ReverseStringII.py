"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Input: s = "abcdefg", k = 2   /   Output: "bacdfeg"
Restrictions:
    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]
"""

class Solution:
    def reverseStr(self, _String, k):
        inputString = list(_String)
        if k == 1:
            return inputString
        elif len(inputString) == k:
            return inputString[::-1]

        for index in range(0, len(inputString)-1, k*2):
            inputString[index:index+k] = inputString[index+(k-1):index-1:-1]
            first, second = inputString[index], inputString[index+1]
            inputString[index], inputString[index + 1] = second, first

        return ''.join(inputString)

if __name__ == '__main__':
    s = Solution()
    inputString = "abcdefg"
    k = 2
    print(s.reverseStr(inputString, k))

    inputString = "abcdef"
    k = 3
    print(s.reverseStr(inputString, k))
