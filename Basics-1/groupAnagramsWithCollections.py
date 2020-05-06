"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
import collections
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

if __name__ == '__main__':
    s = Solution()
    anagramList = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(anagramList))
