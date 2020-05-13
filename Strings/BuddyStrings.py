"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
Input: A = "ab", B = "ba"  /  Output: true
Input: A = "ab", B = "ab"  /  Output: false
Input: A = "aa", B = "aa"  /  Output: true
Input: A = "aaaaaaabc", B = "aaaaaaacb"  /  Output: true
Input: A = "", B = "aa"  /  Output: false
Note:
    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A and B consist only of lowercase letters.
"""

class Solution:
    def buddyStrings(self, strA, strB):
        if len(strA) != len(strB):
            return False
        elif sorted(strA) != sorted(strB):
            return False
        elif strA == strB and len(set(strA)) == len(strA):
            return False

        count = 0
        length = len(strA)
        for index in range(length):
            if strA[index] != strB[index]:
                count += 1
                if count == 3:
                    return False
        return True

if __name__ == '__main__':
    s = Solution()
    strA = "aaaaaaabc"
    strB = "aaaaaaacb"
    print(s.buddyStrings(strA, strB))

    strA = "ab"
    strB = "ab"
    print(s.buddyStrings(strA, strB))

    strA = "aa"
    strB = "aa"
    print(s.buddyStrings(strA, strB))

    strA = "abc"
    strB = "bca"
    print(s.buddyStrings(strA, strB))
