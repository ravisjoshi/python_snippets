"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
You need to return whether the student could be rewarded according to his attendance record.
Input: "PPALLP"  /  Output: True
Input: "PPALLL"  /  Output: False
"""

class Solution:
    def checkRecord(self, inputString):
        return False if inputString.count('A') > 1 or 'LLL' in inputString else True

    def checkRecord_method2(self, inputString):
        if inputString.count('A') > 1 or 'LLL' in inputString:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    inputString = "PPALLP"
    print(s.checkRecord(inputString))

    inputString = "PPALLL"
    print(s.checkRecord(inputString))
