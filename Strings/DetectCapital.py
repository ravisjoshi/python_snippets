"""
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Input: "USA"  /  Output: True
Input: "FlaG"  /  Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

class Solution:
    def detectCapitalUse(self, word):
        if len(word) == 1:
            return True
        flag = True
        for index in range(1, len(word)):
            if word[0].isupper() and word[1].isupper():
                if word[index].isupper():
                    flag = True
                else:
                    return False
            if word[0].isupper() and word[1].islower():
                if word[index].islower():
                    flag = True
                else:
                    return False
            if word[0].islower():
                if word[index].isupper():
                    return False
        return flag

    def detectCapitalUse_method2(self, word):
        return True if word == word.capitalize() or word == word.upper() or word == word.lower() else False

    def detectCapitalUse_method3(self, word):
        return all(ch.isupper() for ch in word) or all(ch.islower() for ch in word[1:])

if __name__ == '__main__':
    s = Solution()
    word = 'USA'
    print(s.detectCapitalUse(word))
