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

Example: Given binary tree [1,2,3,4,null,null,5],
      1
     / \
   2    3
  /      \
4         5
return its minimum depth = 3.
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
        return self._min_depth(root, 1)

    def _min_depth(self, cur_node, count):
        if not cur_node:
            return
        else:
            left = self._min_depth(cur_node.left, count + 1)
            right = self._min_depth(cur_node.right, count + 1)

        if not left and right: return right
        if not right and left: return left
        if left and right: return min(left, right)

        return count


# [1,2,3,4,null,null,5] ==> 3