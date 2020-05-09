"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
s = "leetcode"  /  return 0.
s = "loveleetcode"  /  return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s):
        visited = set()
        for index in range(len(s)):
            if s[index] not in visited:
                visited.add(s[index])
                if s.count(s[index]) == 1:
                    return index
        return -1

if __name__ == '__main__':
    s = Solution()
    inputString = "leetcode"
    print(s.firstUniqChar(inputString))
