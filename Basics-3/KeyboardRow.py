"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Input: ["Hello", "Alaska", "Dad", "Peace"]  /  Output: ["Alaska", "Dad"]
Note:
    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
"""

class Solution:
    def findWords(self, words):
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        res1, res2, res3, result = [], [], [], []
        for word in words:
            for w in word:
                res1.append(w.lower() in row1)
                res2.append(w.lower() in row2)
                res3.append(w.lower() in row3)
            if all(res1) or all(res2) or all(res3):
                result.append(word)
            res1, res2, res3 = [], [], []

        return result

