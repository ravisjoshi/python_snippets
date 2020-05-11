"""
Input: flower flow flight
Output: fl

Input: dog racecar car
Output: ""
"""
class Solution:
    def longestCommonPrefix(self, strs):
        common_prefix = ""
        try:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return common_prefix
                common_prefix += strs[0][i]
        except IndexError:
            pass
        return common_prefix

if __name__ == '__main__':
    myStr = input('Enter the string:- ').rstrip().split()
    s = Solution()
    print(s.longestCommonPrefix(myStr))
