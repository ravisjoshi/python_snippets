"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example: Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if not cur_node.left:
                cur_node.left = TreeNode(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if not cur_node.right:
                cur_node.right = TreeNode(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print('Element {} already in tree!'.format(value))

    def print_tree(self):
        if not self.root:
            print('Tree is empty!')
        else:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node:
            print(cur_node.value, end=' ')
            self._print_tree(cur_node.left)
            self._print_tree(cur_node.right)


    def hasPathSum(self, root, _sum):
        if not root:
            return 0
        elif (_sum - root.val) == 0 and not root.left and not root.right:
            return True

        x = self.hasPathSum(root.left, _sum-root.val)
        y = self.hasPathSum(root.right, _sum-root.val)
        if x or y:
            return True
        else:
            return False

if __name__ == '__main__':
    obj = Solution()
    node_list = [5, 4, 8, 11, 13, 4, 7, 2, 1]
    for value in node_list:
        obj.insert(value)
    #obj.print_tree()

