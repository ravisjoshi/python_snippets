"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
Input: nums = [1,2,2,4]  /  Output: [2,3]

Note:
    The given array size will in the range [2, 10000].
    The given array's numbers won't have any order.
"""

class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        result = [0, 0]
        for index in range(1, len(nums)+1):
            if nums.count(index) == 2:
                result[0] = index
        sums = (n * (n + 1)) // 2
        result[-1] = sums - abs(sum(nums) - result[0])

        return result

    def findErrorNums_method2(self, nums):
        n = len(nums)
        return [sum(nums) - sum(set(nums)), n * (n + 1) // 2 - sum(set(nums))]

if __name__ == '__main__':
    s = Solution()
    numList = [1, 3, 3]
    print(s.findErrorNums(numList))
