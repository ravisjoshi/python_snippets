"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
"""
from time import sleep

class Solution:
    def notInplaceMerge(self, arr1, m, arr2, n):
        if not arr1 and not arr2:
            return []
        finalArray = []
        i = j = 0
        while i < m and j < n:
            if arr1[i] == arr2[j]:
                finalArray.append(arr1[i])
                finalArray.append(arr2[j])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                finalArray.append(arr1[i])
                i += 1
            else:
                finalArray.append(arr2[j])
                j += 1
        while i < m and not j < n:
            finalArray.append(arr1[i])
            i += 1
        while j < n and not i < m:
            finalArray.append(arr2[j])
            j += 1

        print(finalArray)


    def merge(self, arr1, m, arr2, n):
        # Do not return anything, modify nums1 in-place instead.
        arr1[m:] = arr2
        arr1.sort()
        print(arr1)

if __name__ == '__main__':
    s = Solution()
    arr1 = [1, 2, 3, 0, 0, 0]
    m = 3
    arr2 = [2, 5, 6]
    n = 3
    s.merge(arr1, m, arr2, n)
    # print('Expected: [1, 2, 2, 3, 5, 6]', end='\n------------------------\n')
    # # -----------------------------------------------------------
    # arr1 = [4, 0, 0, 0, 0, 0]
    # m = 1
    # arr2 = [1, 2, 3, 5, 6]
    # n = 5
    # s.merge(arr1, m, arr2, n)
    # print('Expected: [1, 2, 3, 4, 5, 6]', end='\n------------------------\n')
    # # ------------------------------------------------------------------------
    # arr1 = [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
    # m = 5
    # arr2 = [-1, -1, 0, 0, 1, 2]
    # n = 6
    # s.merge(arr1, m, arr2, n)
    # print('Expected: [-1, -1, -1, 0, 0, 0, 0, 0, 1, 2, 3]', end='\n------------------------\n')
