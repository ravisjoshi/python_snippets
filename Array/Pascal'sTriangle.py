"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        inputList = [[1], [1, 1]]
        for index in range(2, numRows):
            tempList = []
            for num in range(len(inputList[-1])-1):
                if num == 0:
                    tempList.append(1)
                x = inputList[-1][num]+inputList[-1][num+1]
                tempList.append(x)
            tempList.append(1)
            inputList.append(tempList)
        rList = inputList

        return rList

if __name__ == '__main__':
    s = Solution()
    num = 4
    print(s.generate(num))
