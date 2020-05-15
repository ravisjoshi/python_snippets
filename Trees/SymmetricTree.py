"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Follow up: Solve it both recursively and iteratively.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _check_lrt(self, left, right):

        if not left and not right: return True
        if not left or not right: return False
        if left.val != right.val: return False

        return self._check_lrt(left.left, right.right) and self._check_lrt(left.right, right.left)

    def isSymmetric(self, root):
        if not root:
            return True

        return self._check_lrt(root.left, root.right)

