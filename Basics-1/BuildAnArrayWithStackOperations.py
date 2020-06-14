"""
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.
Build the target array using the following operations:
    Push: Read a new element from the beginning list, and push it in the array.
    Pop: delete the last element of the array.
    If the target array is already built, stop reading more elements.

You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.
Return the operations to build the target array.
You are guaranteed that the answer is unique.

Input: target = [1,3], n = 3   /   Output: ["Push","Push","Pop","Push"]
Explanation:
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

Input: target = [1,2,3], n = 3   /   Output: ["Push","Push","Push"]
Input: target = [1,2], n = 4   /   Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.

Input: target = [2,3,4], n = 4   /   Output: ["Push","Pop","Push","Push","Push"]
Constraints:
    1 <= target.length <= 100
    1 <= target[i] <= 100
    1 <= n <= 100
    target is strictly increasing.
"""

class Solution:
    def buildArray(self, target, num):
        output = []
        _len = 0
        for n in range(1, target[-1]+1):
            if n in target: output.append('Push')
            else: output.append('Push'); output.append('Pop')

        return output

"""
['Push', 'Push']
['Push', 'Push', 'Pop', 'Push']
['Push', 'Push', 'Push']
['Push', 'Pop', 'Push', 'Push', 'Push']
"""
if __name__ == '__main__':
    s = Solution()

    target = [1, 2]
    num = 4
    print(s.buildArray(target, num))

    target = [1, 3]
    num = 3
    print(s.buildArray(target, num))

    target = [1, 2, 3]
    num = 3
    print(s.buildArray(target, num))

    target = [2, 3, 4]
    num = 4
    print(s.buildArray(target, num))



