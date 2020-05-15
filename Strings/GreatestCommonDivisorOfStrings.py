"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)
Return the largest string X such that X divides str1 and X divides str2.

Input: str1 = "ABCABC", str2 = "ABC"  /  Output: "ABC"
Input: str1 = "ABABAB", str2 = "ABAB"  /  Output: "AB"
Input: str1 = "LEET", str2 = "CODE"  /  Output: ""
Note:
    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] and str2[i] are English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1, str2):
        while str2:
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            if str2 in str1:
                str1, str2 = str2, str1.replace(str2, "")
            else:
                return ""
        return str1

if __name__ == '__main__':
    s = Solution()
    str1 = "ABABAB"
    str2 = "ABAB"
    print(s.gcdOfStrings(str1, str2))

    str1 = "ABCABC"
    str2 = "ABC"
    print(s.gcdOfStrings(str1, str2))
