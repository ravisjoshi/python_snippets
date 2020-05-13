"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]   /   Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
Note:
    1 <= paragraph.length <= 1000.
    0 <= banned.length <= 100.
    1 <= banned[i].length <= 10.
    The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
    paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
    There are no hyphens or hyphenated words.
    Words only consist of letters, never apostrophes or other punctuation symbols.
"""

class Solution:
    def mostCommonWord(self, paragraph, banned):
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")

        newPara = paragraph.lower()
        paraList = newPara.split(" ")
        unique_words = set(paraList)
        count_dict = {}
        for word in unique_words:
            if word not in banned and word not in '':
                count_dict.update({word: paraList.count(word)})
        maxCount = max(count_dict.values())
        for key in count_dict:
            if count_dict[key] == maxCount:
                return key

if __name__ == '__main__':
    s = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(s.mostCommonWord(paragraph, banned))

    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    print(s.mostCommonWord(paragraph, banned))
