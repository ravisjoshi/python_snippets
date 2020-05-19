"""
Given two arrays, write a function to compute their intersection.

Input: nums1 = [1,2,2,1], nums2 = [2,2]   /   Output: [2]
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]   /   Output: [9,4]

Note: Each element in the result must be unique. The result can be in any order.
"""
from time import sleep

class Solution:
    def intersection(self, num1, num2):
        snum1, snum2 = list(set(num1)), list(set(num2))
        result = []
        i = 0
        for num in snum1:
            if num in snum2 and num not in result:
                result.append(snum1[i])
                i += 1

        return result

if __name__ == '__main__':
    s = Solution()
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    # print(s.intersection(nums1, nums2))
    #
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    # print(s.intersection(nums1, nums2))

    nums1 = [54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41]
    nums2 = [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]

    print(s.intersection(nums1, nums2))


