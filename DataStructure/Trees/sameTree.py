"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.isSameTree(t1.left, t2. left) and self.isSameTree(t1.right, t2.right)

if __name__ == '__main__':
    obj = Solution()
    # t1NodeValues = [1, 2, 3]
    # t2NodeValues = [1, 2, 3]
    print(obj.isSameTree(t1, t2))

    # t1 = [1, 2]
    # t2 = [1, null, 2]
    # print(obj.isSameTree(t1, t2))

    # t1 = [1, 2, 1]
    # t2 = [1, 1, 2]
    # print(obj.isSameTree(t1, t2))
