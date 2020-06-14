"""
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.

Input: nums = [1,2,3,4]  /  Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

Input: nums = [1,1,2,3]  /  Output: [1,3,3]

Constraints:
    2 <= nums.length <= 100
    nums.length % 2 == 0
    1 <= nums[i] <= 100
"""


class Solution:

    def decompressRLElist(self, nums):
        res = []
        for i in range(0, len(nums), 2):
            res += [nums[i+1]] * nums[i]  # Notice [] placement in here
        return res

    def decompressRLElist_another_approach(self, nums):
        res = []
        x = [nums[i] for i in range(0, len(nums), 2)]
        y = [nums[j] for j in range(1, len(nums), 2)]

        for i, j in zip(x, y):
            for n in range(i):
                res.append(j)
        return res


s = Solution()

nums = [1, 2, 3, 4]
print(s.decompressRLElist(nums))


