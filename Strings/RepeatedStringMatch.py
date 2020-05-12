"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
Note: The length of A and B will be between 1 and 10000.
"""


class Solution:
    def repeatedStringMatch(self, _strA, _strB):
        _len_strA = len(_strA)
        _len_strB = len(_strB)

        if set(_strA) >= set(_strB):
            if _len_strA > _len_strB and _strB in _strA:
                return 1
            start = _len_strB // _len_strA
            while start <= _len_strB:
                if _strB in (_strA * start):
                    return start
                start += 1
        return -1

if __name__ == '__main__':
    s = Solution()
    strA = 'abcd'
    strB = 'cdabcdab'
    print(s.repeatedStringMatch(strA, strB))  # 3

    strA = "aaaaaaaaaaaaaaaaaaaaaab"
    strB = "ba"
    print(s.repeatedStringMatch(strA, strB))  # 2

    strA = "abcd"
    strB = "bc"
    print(s.repeatedStringMatch(strA, strB))  # 1
