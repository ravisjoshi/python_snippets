"""
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

Input: queries = ["cbd"], words = ["zaaaz"]  /  Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]  /  Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

Constraints:
    1 <= queries.length <= 2000
    1 <= words.length <= 2000
    1 <= queries[i].length, words[i].length <= 10
    queries[i][j], words[i][j] are English lowercase letters.
"""

class Solution:
    def numSmallerByFrequency(self, queries, words):
        def f(string):
            ss = sorted(string)
            return ss.count(ss[0])

        answer = []
        for q in queries:
            count = 0
            x = f(q)
            for w in words:
                if x < f(w):
                    count += 1
            answer.append(count)

        return answer


s = Solution()

queries, words = ["bbb","cc"], ["a","aa","aaa","aaaa"]
print(s.numSmallerByFrequency(queries, words))

# queries, words = ["cbd"], ["zaaaz"]
# print(s.numSmallerByFrequency(queries, words))
