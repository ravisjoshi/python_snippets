"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
Return the power of the string.
Input: s = "leetcode"  /  Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Input: s = "abbcccddddeeeeedcba"  /  Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Input: s = "triplepillooooow"  /  Output: 5
Input: s = "hooraaaaaaaaaaay"  /  Output: 11
Input: s = "tourist"  /  Output: 1
Constraints:
    1 <= s.length <= 500
    s contains only lowercase English letters.
"""

class Solution:
    def maxPower(self, _string):
        if len(_string) == 1:
            return 1
        elif len(set(_string)) == 1:
            return len(_string)
        count_list = {}
        count = 1
        prev = _string[0]
        for index in range(1, len(_string)):
            if prev == _string[index]:
                count += 1
                prev = _string[index]
            else:
                if (prev not in count_list) or (count_list[prev] < count):
                    count_list.update({prev: count})
                count = 1
                prev = _string[index]

        if (prev not in count_list) or (count_list[prev] < count):
            count_list.update({prev: count})
        return max(count_list.values())

if __name__ == '__main__':
    s = Solution()
    _string = "leetcode"
    print(s.maxPower(_string))

    _string = "abbcccddddeeeeedcba"
    print(s.maxPower(_string))

    _string = "j"
    print(s.maxPower(_string))

    _string = "cc"
    print(s.maxPower(_string))

    _string = "aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz"
    print(s.maxPower(_string))