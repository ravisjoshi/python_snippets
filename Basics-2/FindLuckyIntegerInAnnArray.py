"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

Input: arr = [2,2,3,4]  /  Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Input: arr = [1,2,2,3,3,3]  /  Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Input: arr = [2,2,2,3,3]  /  Output: -1
Explanation: There are no lucky numbers in the array.
Input: arr = [5]  /  Output: -1
Input: arr = [7,7,7,7,7,7,7]  /  Output: 7
Constraints:
    1 <= arr.length <= 500
    1 <= arr[i] <= 500
"""

class Solution:
    def findLucky(self, arr):
        if len(set(arr)) == 1 and arr[0] == len(arr):
            return arr[0]
        s_arr = sorted(arr)
        output = {}
        prev = s_arr[0]
        count = 1
        for index in range(1, len(s_arr)):
            if prev == s_arr[index]:
                count += 1
            else:
                output.update({prev: count})
                prev = s_arr[index]
                count = 1
        output.update({prev: count})

        result = [key for key in output if key == output[key]]
        return -1 if not result else max(result)

if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 2, 3, 3, 3]
    print(s.findLucky(arr))

    arr = [2, 2, 2, 3, 3]
    print(s.findLucky(arr))

    arr = [2, 2, 3, 4]
    print(s.findLucky(arr))

    arr = [7, 7, 7, 7, 7, 7, 7]
    print(s.findLucky(arr))

