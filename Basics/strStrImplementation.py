"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "hello", needle = "ll"  /  Output: 2

Input: haystack = "aaaaa", needle = "bba"  /  Output: -1
"""

class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        stack_dict = {}
        for index, value in enumerate(haystack):
            stack_dict.update({index: value})
        print(stack_dict)

        if needle in haystack:
            for _index, value in enumerate(needle):

        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    haystack = "hello"
    needle = "ll"
    print(s.strStr(haystack, needle))

