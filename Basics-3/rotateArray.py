"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
Follow up:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
---
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Constraints:
    1 <= nums.length <= 2 * 10^4
    It's guaranteed that nums[i] fits in a 32 bit-signed integer.
    k >= 0
"""

class Solution:
    # Complexity n*n --> Time Limit Exceeded
    def rotateMethod1(self, numList, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(numList)
        # 1 <= length <= 2 * 10 ^ 4
        for index in range(k):
            temp = numList[-1]
            for numIndex in range(len(numList)-1, 0, -1):
                numList[numIndex] = numList[numIndex-1]
            numList[0] = temp
        print(numList)

    def notInPlace_rotate(self, numList, k):
        x = k+1
        numList = numList[x:] + numList[:x]
        print(numList)

    def rotate(self, numList, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(k):
            numList.insert(0, numList.pop(-1))

        print(numList)

if __name__ =='__main__':
    s = Solution()
    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 4
    s.rotate(numList, k)
    # numList = [-1, -100, 3, 99]
    # k = 2
    # s.rotate(numList, k)

