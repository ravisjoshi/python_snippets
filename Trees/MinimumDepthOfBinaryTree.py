"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example: Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        elif root and not root.left and not root.right:
            return 1
        else:
            count = 1
            left_depth = self._min_depth(root.left, count)
            right_depth = self._min_depth(root.right, count)

        return min(left_depth, right_depth)

    def _min_depth(self, cur_node, count):
        if not cur_node:
            return count
        else:
            count += 1
            if cur_node.left:
                self._min_depth(cur_node.left, count)
            elif cur_node.right:
                self._min_depth(cur_node.right, count)
            else:
                return count
