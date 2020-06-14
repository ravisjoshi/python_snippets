"""
Given a string s. You should re-order the string using the following algorithm:
    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
Return the result string after sorting s with this algorithm.

Input: s = "aaaabbbbcccc"  /  Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Input: s = "rat"  /  Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Input: s = "leetcode"  /  Output: "cdelotee"

Input: s = "ggggggg"  /  Output: "ggggggg"
Input: s = "spo"  /  Output: "ops"

Constraints:
    1 <= s.length <= 500
    s contains only lower-case English letters.
"""

class Solution:
    def sortString(self, s):
        s = list(s)
        result = ''
        while s:
            for letter in sorted(set(s)):
                s.remove(letter)
                result += letter
            for letter in sorted(set(s), reverse=True):
                s.remove(letter)
                result += letter
        return result

    def sortString_BruteForce(self, _string):
        res = []
        sorted_s = sorted(_string)

        while sorted_s:
            temp = "".join(sorted_s)
            while len(temp) > 0:
                smallest = min(temp)
                res.append(smallest)
                temp = temp.replace(smallest, '')
                sorted_s.remove(smallest)
            temp = "".join(sorted_s)
            while len(temp) > 0:
                largest = max(temp)
                res.append(largest)
                temp = temp.replace(largest, '')
                sorted_s.remove(largest)

        print("".join(res))


s = Solution()
_string = "aaaabbbbcccc"
print(s.sortString(_string))


