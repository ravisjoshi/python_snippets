"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Input: a = "11", b = "1"  /  Output: "100"
Input: a = "1010", b = "1011"  /  Output: "10101"
"""

class Solution:
    def addBinary(self, string_a, string_b):
        if string_a == '0' and string_b == '0':
            return '0'
        result = ""
        stringA = string_a if len(string_a) > len(string_b) else string_b
        stringB = string_b if len(string_b) < len(string_a) else string_a
        length = len(stringA)
        position = -1
        remainder = 0

        # "101111" - "10"   -    "110001"
        for i in range(length-1, -1, -1):
            if abs(position) <= len(stringB):
                if int(stringA[i]) + int(stringB[position]) + remainder == 0:
                    remainder = 0
                    char = 0
                    result += str(char)
                elif int(stringA[i]) + int(stringB[position]) + remainder == 1:
                    remainder = 0
                    char = 1
                    result += str(char)
                elif int(stringA[i])+int(stringB[position])+remainder == 2:
                    remainder = 1
                    char = 0
                    result += str(char)
                elif int(stringA[i])+int(stringB[position])+remainder == 3:
                    remainder = 1
                    char = 1
                    result += str(char)
                position -= 1

            elif abs(position) >= len(stringB) and int(stringA[i]) + remainder == 0:
                remainder = 0
                char = 0
                result += str(char)
            elif abs(position) >= len(stringB) and int(stringA[i]) + remainder == 1:
                remainder = 0
                char = 1
                result += str(char)
            elif abs(position) >= len(stringB) and int(stringA[i]) + remainder == 2:
                remainder = 1
                char = 0
                result += str(char)

        if remainder == 1:
            result += str(remainder)

        return result[::-1]

if __name__ == '__main__':
    s = Solution()
    # stringA = "1"
    # stringB = "111"
    # stringA = "11"
    # stringB = "1"
    # stringA = "1010"
    # stringB = "1011"
    # stringA = "100"
    # stringB = "110010"
    stringA = "101111"
    stringB = "10"

    print(s.addBinary(stringA, stringB))
