"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Input: S = "a1b2"  /  Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
Input: S = "3z4"  /  Output: ["3z4", "3Z4"]
Input: S = "12345"  /  Output: ["12345"]

Note:
    S will be a string with length between 1 and 12.
    S will consist only of letters or digits.
"""

class Solution:
    def letterCasePermutation(self, _string):
        res = ['']
        for char in _string:
            if char.isdigit():
                for i in range(len(res)):
                    res[i] = res[i]+char
            else:
                for c in range(len(res)):
                    temp = res[c]
                    res[c] = temp+char
                    res.append(temp + char.swapcase())

        return res


s = Solution()

_string = "abcd"
print(s.letterCasePermutation(_string))




