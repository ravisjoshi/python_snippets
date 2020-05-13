"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
Input: "ab-cd"   /   Output: "dc-ba"
Input: "a-bC-dEf-ghIj"   /   Output: "j-Ih-gfE-dCba"
Input: "Test1ng-Leet=code-Q!"   /   Output: "Qedo1ct-eeLg=ntse-T!"
Note:
    S.length <= 100
    33 <= S[i].ASCIIcode <= 122
    S doesn't contain \ or "
"""

class Solution:
    def reverseOnlyLetters(self, _string):
        length = len(_string)
        non_char_list = {}
        newstr = []
        for index in range(length):
            if not (ord('a') <= ord(_string[index]) <= ord('z') or ord('A') <= ord(_string[index]) <= ord('Z')):
                non_char_list.update({index: _string[index]})
            else:
                newstr.append(_string[index])
        rev_string = newstr[::-1]
        for key in non_char_list.keys():
            rev_string.insert(key, non_char_list[key])

        return "".join(rev_string)


if __name__ == '__main__':
    s = Solution()
    _string = "Test1ng-Leet=code-Q!"
    print(s.reverseOnlyLetters(_string))

    _string = "ab-cd"
    print(s.reverseOnlyLetters(_string))
