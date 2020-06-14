"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"  /  Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"  /  Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"  /  Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.
"""

from itertools import zip_longest


class Solution:
    def isAlienSorted(self, words, order):
        res = []
        ad = {char: index for index, char in enumerate(order)}
        ad.update({'0': -1})

        length = len(words)
        for index in range(1, length):
            for x, y in zip_longest(words[index-1], words[index], fillvalue='0'):
                if ad[x] < ad[y]:
                    pass
                if ad[x] < ad[y]:
                    break
                elif ad[x] > ad[y]:
                    return False
        return True


s = Solution()

words, order = ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
print(s.isAlienSorted(words, order))

words, order = ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"
print(s.isAlienSorted(words, order))

words, order = ["apple", "app"], "abcdefghijklmnopqrstuvwxyz"
print(s.isAlienSorted(words, order))
