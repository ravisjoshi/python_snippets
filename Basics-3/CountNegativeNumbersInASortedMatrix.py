"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]  /  Output: 8
Explanation: There are 8 negatives number in the matrix.

Input: grid = [[3,2],[1,0]]  /  Output: 0
Input: grid = [[1,-1],[-1,-1]]  /  Output: 3
Input: grid = [[-1]]  /  Output: 1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""
class Solution:
    def countNegatives(self, grid):
        column = len(grid[0])
        row = len(grid)
        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] < 0:
                    count += 1
        return count