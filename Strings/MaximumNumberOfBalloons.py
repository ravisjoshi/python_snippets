"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
Input: text = "nlaebolko"  /  Output: 1
Input: text = "loonbalxballpoon"  /  Output: 2
Input: text = "leetcode"  /  Output: 0
Constraints:
    1 <= text.length <= 10^4
    text consists of lower case English letters only.
"""

class Solution:
    def maxNumberOfBalloons(self, text):
        b_dict = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in b_dict:
                b_dict[char] += 1
        return min(b_dict["b"], b_dict["a"], b_dict["l"] // 2, b_dict["o"] // 2, b_dict["n"])


if __name__ == '__main__':
    s = Solution()
    text = "loonbalxballpoon"
    print(s.maxNumberOfBalloons(text))

    text = "nlaebolko"
    print(s.maxNumberOfBalloons(text))

    text = "leetcode"
    print(s.maxNumberOfBalloons(text))
