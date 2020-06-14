"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]  /  Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]  /  Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Input: matrix = [[7,8],[1,2]]  /    Output: [7]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5.
    All elements in the matrix are distinct.
"""

from time import sleep

class Solution:
    def luckyNumbers(self, matrix):
        min_row = []
        max_col = []
        for i in range(0, len(matrix)):
            min_row.append(min(matrix[i]))

        for col in zip(*matrix):
            max_col.append(max(col))

        res = []
        for min_val in min_row:
            if min_val in max_col:
                res.append(min_val)
        return res


s = Solution()

matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
print(s.luckyNumbers(matrix))

matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
print(s.luckyNumbers(matrix))

matrix = [[7, 8], [1, 2]]
print(s.luckyNumbers(matrix))



