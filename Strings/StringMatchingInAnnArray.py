"""
Given an array of string words. Return all strings in words which is substring of another word in any order.
String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Input: words = ["mass","as","hero","superhero"]   /   Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Input: words = ["leetcode","et","code"]   /   Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Input: words = ["blue","green","bu"]   /   Output: []
Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 30
    words[i] contains only lowercase English letters.
    It's guaranteed that words[i] will be unique.
"""

class Solution:
    def stringMatching(self, words):
        r_list = []
        for index in range(len(words)):
            for word in words:
                if words[index] in word and words[index] != word:
                    r_list.append(words[index])
                    break
        return r_list

if __name__ == '__main__':
    s = Solution()
    words = ["mass","as","hero","superhero"]
    print(s.stringMatching(words))

    words = ["leetcode","et","code"]
    print(s.stringMatching(words))

    words = ["blue","green","bu"]
    print(s.stringMatching(words))

    words = ["leetcoder","leetcode","od","hamlet","am"]
    print(s.stringMatching(words))
