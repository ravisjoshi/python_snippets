"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Input: [1,2,3]  /  Output: 6
Input: [1,2,3,4]  /  Output: 24
Note:
    The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        if nums[-1] == 0 and 0 in nums: return 0
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

s = Solution()

arr = [903,606,48,-474,313,-672,872,-833,899,-629,558,-368,231,621,716,-41,-418,204,-1,883,431,810,452,-801,19,978,542,930,85,544,-784,-346,923,224,-533,-473,499,-439,-925,171,-53,247,373,898,700,406,-328,-468,95,-110,-102,-719,-983,776,412,-317,606,33,-584,-261,761,-351,-300,825,224,382,-410,335,187,880,-762,503,289,-690,117,-742,713,280,-781,447,227,-579,-845,-526,-403,-714,-154,960,-677,805,230,591,442,-458,-905,832,-285,511,536,-86]
print(s.maximumProduct(arr))

arr = [-4, -3, -2, -1, 60]
print(s.maximumProduct(arr))

arr = [-20, 1, -50, 1, 2, 3, 4, -5]
print(s.maximumProduct(arr))

arr = [1, 2, 3, 4]
print(s.maximumProduct(arr))


