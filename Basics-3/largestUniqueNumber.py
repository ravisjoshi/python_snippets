class Solution:
    def largestUnique(self, numList):
        newList = sorted(list(set(numList)))
        return max([i for i in newList[::-1] if numList.count(i) == 1])

if __name__ == '__main__':
    s = Solution()
    numList = [2, 8, 1, 9, 100, 23, 18, 100, 1, 8]

    print(s.largestUnique(numList))
