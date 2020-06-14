"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Input: [[1,1,0],[1,0,1],[0,0,0]]  /  Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]  /  Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Notes:
    1 <= A.length = A[0].length <= 20
    0 <= A[i][j] <= 1
"""

class Solution:
    def flipAndInvertImage(self, A):
        for row in A:
            for i in range((len(row) + 1) // 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A


    def flipAndInvertImage_BruteForce(self, A):
        res = []
        for row in A:
            res.append(row[::-1])
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j] == 1: res[i][j] = 0
                else:              res[i][j] = 1
        return res


s = Solution()

A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s.flipAndInvertImage(A))

A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s.flipAndInvertImage_BruteForce(A))




