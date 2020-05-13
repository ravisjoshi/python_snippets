"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]   /   Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Input: paths = [["B","C"],["D","B"],["C","A"]]   /   Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".

Input: paths = [["A","Z"]]   /   Output: "Z"
Constraints:
    1 <= paths.length <= 100
    paths[i].length == 2
    1 <= cityAi.length, cityBi.length <= 10
    cityAi != cityBi
    All strings consist of lowercase and uppercase English letters and the space character.
"""

class Solution:
    def destCity(self, paths):
        if len(paths) == 1:
            return paths[0][-1]
        start = []
        end = []
        for path in paths:
            start.append(path[0])
            end.append(path[1])
        return "".join([e for e in end if e not in start])

if __name__ == '__main__':
    s = Solution()
    paths = [["B","C"],["D","B"],["C","A"]]
    print(s.destCity(paths))

    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(s.destCity(paths))
