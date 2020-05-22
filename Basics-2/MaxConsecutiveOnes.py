"""
Given a binary array, find the maximum number of consecutive 1s in this array.
Input: [1,1,0,1,1,1]  /  Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Note:
    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        if len(set(nums)) == 1 and nums[0] == 1:
            return len(nums)
        elif len(set(nums)) == 1 and nums[0] == 0:
            return 0
        count = 0
        output = {1: 0}
        for n in nums:
            if n == 1: count += 1
            else:      count = 0
            if output[1] < count:
                output.update({1: count})

        return output[1]

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print(s.findMaxConsecutiveOnes(nums))

    nums = [1, 1, 1, 1, 1, 1]
    print(s.findMaxConsecutiveOnes(nums))

    nums = [0, 0, 0]
    print(s.findMaxConsecutiveOnes(nums))

    nums = [1]
    print(s.findMaxConsecutiveOnes(nums))

