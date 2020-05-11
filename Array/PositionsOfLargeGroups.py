"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.
Input: "abbxxxxzzy"   /   Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Input: "abc"   /   Output: []
Explanation: We have "a","b" and "c" but no large group.
Input: "abcdddeeeeaabbbcd"   /   Output: [[3,5],[6,9],[12,14]]
Note:  1 <= S.length <= 1000
"""

class Solution:
    def largeGroupPositions(self, inputString):
        output = []
        count, prevIndex = 0, 0
        prev_char = inputString[0]
        for index in range(len(inputString)):
            if inputString[index] == prev_char:
                count += 1
            elif inputString[index] != prev_char and count >= 3:
                output.append([prevIndex, index-1])
                prev_char = inputString[index]
                prevIndex = index
                count = 1
            else:
                prev_char = inputString[index]
                prevIndex = index
                count = 1
        if count >= 3 and prev_char == inputString[-1]:
            output.append([prevIndex, len(inputString) - 1])
        return output


if __name__ == '__main__':
    s = Solution()
    inputString = 'aaa'
    print(s.largeGroupPositions(inputString))
    inputString = 'abcdddeeeeaabbbcd'
    print(s.largeGroupPositions(inputString))
