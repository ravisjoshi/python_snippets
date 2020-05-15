"""
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.

Input: s = "a0b1c2"  /  Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Input: s = "leetcode"  /  Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Input: s = "1229857369"  /  Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Input: s = "covid2019"  /  Output: "c2o0v1i9d"
Input: s = "ab123"  /  Output: "1a2b3"
Constraints:
    1 <= s.length <= 500
    s consists of only lowercase English letters and/or digits.
"""

class Solution:
    def reformat(self, _string):
        if len(_string) == 1:
            return _string
        elif _string.isdigit() or _string.isalpha():
            return ""

        a = d = 0
        x = [len(char) if char.isalpha() else -1 for char in _string]
        a = [c for c in _string if c.isalpha()]
        d = [d for d in _string if d.isdigit()]
        if sum(x) in [-1, 0, 1]:
            if sum(x) == 0:
                return "".join([x+y for x, y in zip(a, d)])
            elif sum(x) == 1:
                return "".join([x + y for x, y in zip(a, d)]) + a[-1]
            elif sum(x) == -1:
                return "".join([x + y for x, y in zip(d, a)]) + d[-1]
        else:
            return ""


if __name__ == '__main__':
    s = Solution()
    _string = "j"
    print(s.reformat(_string))
