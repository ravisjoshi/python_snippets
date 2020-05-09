"""
Write a function that takes a string as input and reverse only the vowels of a string.
Input: "hello"  /  Output: "holle"
Input: "leetcode"  /  Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, input_String):
        inputString = list(input_String)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start, end = 0, len(inputString)-1
        while start < end:
            if inputString[start] in vowels and inputString[end] in vowels:
                inputString[start], inputString[end] = inputString[end], inputString[start]
                start += 1
                end -= 1
            elif inputString[start] not in vowels and inputString[end] not in vowels:
                start += 1
                end -= 1
            elif inputString[start] not in vowels:
                start += 1
            elif inputString[end] not in vowels:
                end -= 1

        return "".join(inputString)

if __name__ == '__main__':
    s = Solution()
    inputString = "Marge, let's \"went.\" I await news telegram."
    print('Output:   {}'.format(s.reverseVowels(inputString)))
    print('Expected: Marge, let\'s "went." i awaIt news telegram.')
    # inputString = "leetcode"
    # print(s.reverseVowels(inputString))
    inputString = "aA"
    print(s.reverseVowels(inputString))
    # inputString = "race a car"
    # print(s.reverseVowels(inputString))
