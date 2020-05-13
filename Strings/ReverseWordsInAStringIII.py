"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Input: "Let's take LeetCode contest"   /   Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, _str):
        _str_list = _str.split()
        _list_len = len(_str_list)
        for index in range(_list_len):
            _str_list[index] = _str_list[index][::-1]

        return ' '.join(_str_list)

if __name__ == '__main__':
    s = Solution()
    _str = "Let's take LeetCode contest"
    print(s.reverseWords(_str))
