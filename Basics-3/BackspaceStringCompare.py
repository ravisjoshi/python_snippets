"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Input: S = "ab#c", T = "ad#c"  /  Output: true
Explanation: Both S and T become "ac".

Input: S = "ab##", T = "c#d#"  /  Output: true
Explanation: Both S and T become "".

Input: S = "a##c", T = "#a#c"  /  Output: true
Explanation: Both S and T become "c".

Input: S = "a#c", T = "b"  /  Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.
Follow up: Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    def finalString(self, _string):
        temp = []
        for s in _string:
            if s == '#' and temp != []:
                temp.pop(-1)
            elif s != '#':
                temp.append(s)
        return temp

    def backspaceCompare(self, S, T):
        return self.finalString(S) == self.finalString(T)


s = Solution()

S, T = "ab#c", "ad#c"
print(s.backspaceCompare(S, T))

S, T = "y#fo##f", "y#f#o##f"
print(s.backspaceCompare(S, T))
