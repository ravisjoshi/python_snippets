"""
Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.



Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]  /  Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]  /  Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.

Input: arr = [10000,10000]  /  Output: [10000,10000]
Input: arr = [2,3,5,7,11,13,17,19]  /  Output: [2,3,5,17,7,11,13,19]

Input: arr = [10,100,1000,10000]  /  Output: [10,100,10000,1000]

Constraints:
    1 <= arr.length <= 500
    0 <= arr[i] <= 10^4
"""

class Solution:
    def sortByBits_BruteForce(self, arr):
        sorted_arr = sorted(arr)
        num_dict = {}
        result = []
        for key, value in zip(sorted_arr, map(bin, sorted_arr)):
            num_dict.update({key: value[2:].count('1')})

        for key, value in sorted(num_dict.items(), key=lambda item: item[1]):
            count = sorted_arr.count(key)
            while count > 0:
                result.append(key)
                count -= 1
        return result

    def sortByBits(self, arr):
        arr = sorted(arr)
        arr.sort(key=lambda x: bin(x).count('1'))
        return arr

s = Solution()
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(s.sortByBits(arr))

arr = [10000, 10000]
print(s.sortByBits(arr))

arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
print(s.sortByBits(arr))













