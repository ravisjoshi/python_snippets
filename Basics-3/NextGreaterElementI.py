"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].  /  Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Input: nums1 = [2,4], nums2 = [1,2,3,4].  /  Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
    All elements in nums1 and nums2 are unique.
    The length of both nums1 and nums2 would not exceed 1000.
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for ni in range(len(nums1)):
            i = nums2.index(nums1[ni])
            for j in range(i, len(nums2)):
                if nums2[j] > nums1[ni]:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)
        return result


s = Solution()
nums1 = [4, 1, 2]; nums2 = [1, 3, 4, 2]  # [-1,3,-1]
print(s.nextGreaterElement(nums1, nums2))

nums1 = [1, 3, 5, 2, 4]; nums2 = [6, 5, 4, 3, 2, 1, 7]
print(s.nextGreaterElement(nums1, nums2))

