"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Input: [5, 4, 3, 2, 1]  /  Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.

Note:
    N is a positive integer and won't exceed 10,000.
    All the scores of athletes are guaranteed to be unique.
"""

class Solution:

    def findRelativeRanks(self, nums):
        index = sorted(range(len(nums)), reverse=True, key=nums.__getitem__)
        for i in range(len(index)):
            if i == 0:
                nums[index[i]] = "Gold Medal"
            elif i == 1:
                nums[index[i]] = "Silver Medal"
            elif i == 2:
                nums[index[i]] = "Bronze Medal"
            else:
                nums[index[i]] = str(i + 1)
        return nums

    def findRelativeRanks_BruteForce(self, nums):
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = []
        new_num = sorted(nums)[::-1]
        maxList = sorted(nums)[::-1][:3]

        for n in nums:
            if n in maxList:
                res.append(medals[maxList.index(n)])
            else:
                res.append(str(new_num.index(n) + 1))
        return res
