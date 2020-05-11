"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
Input: nums = [8,1,2,2,3]   /   Output: [4,0,1,1,3]
Input: nums = [6,5,4,8]   /   Output: [2,1,0,3]
Input: nums = [7,7,7,7]   /   Output: [0,0,0,0]
Constraints:
    2 <= nums.length <= 500
    0 <= nums[i] <= 100
"""

class Solution:
    def smallerNumbersThanCurrentMethod1(self, numList):
        finalList = []
        for index in numList:
            count = 0
            for newIndex in range(len(numList)):
                if index > numList[newIndex]:
                    count += 1
            finalList.append(count)

        return finalList

    def smallerNumbersThanCurrent(self, numList):
        finalList = []
        num_Dict = {sorted(numList)[0]:0}
        print(num_Dict)

if __name__ == '__main__':
    s =Solution()
    numList = [8, 1, 2, 2, 3]
    print(s.smallerNumbersThanCurrent(numList))