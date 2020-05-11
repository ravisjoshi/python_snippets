"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Input: ransomNote = "a", magazine = "b"  /  Output: false
Input: ransomNote = "aa", magazine = "ab"  /  Output: false
Input: ransomNote = "aa", magazine = "aab"  /  Output: true
Constraints: You may assume that both strings contain only lowercase letters.
"""

class Solution:
    def canConstruct(self, ransomNote, magazine):
        rIndex = mIndex = 0
        rlen = len(ransomNote)
        mlen = len(magazine)
        aRansomNote = sorted(ransomNote)
        aMagazine = sorted(magazine)
        while rIndex < rlen and mIndex < mlen:
            if aRansomNote[rIndex] == aMagazine[mIndex]:
                rIndex += 1
                mIndex += 1
            elif not aRansomNote[rIndex] == aMagazine[mIndex]:
                mIndex += 1

        if rIndex == len(aRansomNote):
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    ransomNote = "aab"
    magazine = "baa"
    print(s.canConstruct(ransomNote, magazine))
