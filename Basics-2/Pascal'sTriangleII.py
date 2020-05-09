"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Input: 3  /  Output: [1,3,3,1]
"""


class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        inputList = [[1], [1, 1]]
        for index in range(1, rowIndex):
            tempList = []
            for num in range(len(inputList[-1])-1):
                if num == 0:
                    tempList.append(1)
                x = inputList[-1][num]+inputList[-1][num+1]
                tempList.append(x)
            tempList.append(1)
            inputList.append(tempList)
        rList = inputList

        return rList[-1]

if __name__ == '__main__':
    s = Solution()
    rowIndex = 3
    print(s.getRow(rowIndex))
