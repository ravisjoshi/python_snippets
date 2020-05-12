"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.
Input: "Hello, my name is John"  /  Output: 5
"""

class Solution:
    def countSegments(self, _str):
        count = 0
        prev_char = ' '
        for char in _str:
            if char != ' ' and prev_char == ' ':
                count += 1
            prev_char = char

        return count

if __name__ == '__main__':
    s =Solution()
    inputString = "Hello, my name is John"
    print(s.countSegments(inputString))
