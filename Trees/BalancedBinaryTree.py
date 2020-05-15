"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1: Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2: Given the following tree [1,2,2,3,3,null,null,4,4]:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _isBalanced(self, cur_node):
        if not cur_node:
            return 0
        left_height = self._isBalanced(cur_node.left)
        right_height = self._isBalanced(cur_node.right)
        self.ans = max(self.ans, abs(left_height - right_height))
        return max(left_height, right_height) + 1


    def isBalanced(self, root):
        if not root:
            return True
        self.ans = 0
        self.ans = self._isBalanced(root)
        if self.ans > 1:
            return False
        else:
            return True


