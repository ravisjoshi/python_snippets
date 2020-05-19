"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example: Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
"""

"""
from random import randint

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class binaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def levelOrder(self):
        if not self.root:
            print('Tree is empty!')
        else:
            self.output = []
            height = 1
            self._leetCode_levelorder_print_tree(self.root, height)
            return self.output

    def _leetCode_levelorder_print_tree(self, cur_node, height):
        if cur_node:
            if len(self.output) < height:
                self.output.append([cur_node.val])
            else:
                self.output[height-1].append(cur_node.val)

            self._leetCode_levelorder_print_tree(cur_node.left, height+1)
            self._leetCode_levelorder_print_tree(cur_node.right, height+1)

if __name__ == '__main__':

    # [3, 9, 20, null, null, 15, 7]  /  [[3],[9,20],[15,7]]
    # tree = binaryTree(3)
    # tree.root.left = TreeNode(9)
    # tree.root.right = TreeNode(20)
    # tree.root.right.left = TreeNode(15)
    # tree.root.right.right = TreeNode(7)
    # print(tree.print_tree())

    # [1,2,3,4,null,null,5]  /  [[1],[2,3],[4,5]]
    tree = binaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.right.right = TreeNode(5)
    print(tree.levelOrder())

    # [1,2,3,4,0,0,5]  /  [[1],[2,3],[4,5]]
    tree = binaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(0)
    tree.root.right.left = TreeNode(0)
    tree.root.right.right = TreeNode(5)
    tree.root.left.left.left = TreeNode(6)
    tree.root.left.left.right = TreeNode(0)
    tree.root.left.right.left = TreeNode(0)
    tree.root.left.right.right = TreeNode(7)
    tree.root.right.right.left = TreeNode(8)
    tree.root.right.right.right = TreeNode(9)
    print(tree.levelOrder())

