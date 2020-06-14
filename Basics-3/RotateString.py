"""
We are given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Input: A = 'abcde', B = 'cdeab'  /  Output: true
Input: A = 'abcde', B = 'abced'  /  Output: false

Note: A and B will have length at most 100.
"""

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        elif len(A) != len(B):
            return False

        A, B = list(A), list(B)
        for r in range(len(A) - 1):
            A.append(A.pop(0))
            if A == B:
                return True
        return False

s = Solution()
A, B = 'abcde', 'cdeab'
print(s.rotateString(A, B))
