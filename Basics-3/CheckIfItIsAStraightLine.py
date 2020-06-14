"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]  /  Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]  /  Output: false

Constraints:
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""

class Solution:
    def checkStraightLine(self, coordinates):
        x_diff = coordinates[1][0] - coordinates[0][0]
        y_diff = coordinates[1][1] - coordinates[0][1]

        for i in range(len(coordinates)):
            if y_diff * (coordinates[i][0] - coordinates[1][0]) != x_diff * (coordinates[i][1] - coordinates[1][1]):
                return False

        return True

s = Solution()

coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(s.checkStraightLine(coordinates))

coordinates = [[2, 1], [4, 2], [6, 3]]
print(s.checkStraightLine(coordinates))

coordinates = [[0, 0], [0, 1], [0, -1]]
print(s.checkStraightLine(coordinates))

coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
print(s.checkStraightLine(coordinates))








