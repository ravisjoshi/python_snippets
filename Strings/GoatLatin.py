"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
The rules of Goat Latin are as follows:
    If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
    For example, the word 'apple' becomes 'applema'.
    If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
    For example, the word "goat" becomes "oatgma".
    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.
Input: "I speak Goat Latin"   /   Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
Notes:
    S contains only uppercase, lowercase and spaces. Exactly one space between each word.
    1 <= S.length <= 150.
"""

class Solution:
    def toGoatLatin(self, _string):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = _string.split()
        length = len(s_list)
        for index in range(1, length+1):
            temp = s_list.pop(index-1)
            print(temp)
            if temp[0] in vowels:
                newWord = temp+'ma'+'a'*index
                s_list.insert(index-1, newWord)
            else:
                newWord = temp[1:] + temp[0] + 'ma' + 'a' * index
                s_list.insert(index-1, newWord)

        return " ".join(s_list)


if __name__ == '__main__':
    s = Solution()
    # _string = 'I speak Goat Latin'
    # print(s.toGoatLatin(_string))

    _string = "The quick brown fox jumped over the lazy dog"
    print(s.toGoatLatin(_string))


