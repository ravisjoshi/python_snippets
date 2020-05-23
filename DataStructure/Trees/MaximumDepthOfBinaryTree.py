"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _depth(self, cur_node, height):
        if not cur_node:
            return height
        else:
            left_height = self._depth(cur_node.left, height+1)
            right_height = self._depth(cur_node.right, height+1)

        return max(left_height, right_height)

    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return self._depth(root, 0)


