"""

"""
from random import randint

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class binaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

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
            print('\npre-order:-')
            self._preorder_print_tree(self.root)
            print('\nin-order:-')
            self._inorder_print_tree(self.root)
            print('\npost-order:-')
            self._postorder_print_tree(self.root)
            print('\nlevel-order:-')
            print(self.root.value, end=' -> ')
            self._levelorder_print_tree(self.root)

    def _preorder_print_tree(self, cur_node):
        """
        Until all nodes are traversed −
        Step 1 − Visit root node.
        Step 2 − Recursively traverse left subtree.
        Step 3 − Recursively traverse right subtree.
        """
        if cur_node:
            print(cur_node.value, end=' -> ')
            self._preorder_print_tree(cur_node.left)
            self._preorder_print_tree(cur_node.right)

    def _inorder_print_tree(self, cur_node):
        """
        Until all nodes are traversed −
        Step 1 − Recursively traverse left subtree.
        Step 2 − Visit root node.
        Step 3 − Recursively traverse right subtree.
        """
        if cur_node:
            self._preorder_print_tree(cur_node.left)
            print(cur_node.value, end=' -> ')
            self._preorder_print_tree(cur_node.right)

    def _postorder_print_tree(self, cur_node):
        """
        Until all nodes are traversed −
        Step 1 − Recursively traverse left subtree.
        Step 2 − Recursively traverse right subtree.
        Step 3 − Visit root node.
        """
        if cur_node:
            self._preorder_print_tree(cur_node.left)
            self._preorder_print_tree(cur_node.right)
            print(cur_node.value, end=' -> ')

    def _levelorder_print_tree(self, cur_node):
        if cur_node:
            if cur_node.left:
                print(cur_node.left.value, end=' -> ')
            if cur_node.right:
                print(cur_node.right.value, end=' -> ')
            self._levelorder_print_tree(cur_node.left)
            self._levelorder_print_tree(cur_node.right)


# Create random array
# def create_array(length=15, max=50):
#     arr = []
#     for _ in range(length):
#         arr.append(randint(0, max))
#     print(arr)
# create_array()

if __name__ == '__main__':
    # s = binaryTree()
    # arr = [30, 25, 50, 15, 16, 41, 11, 24, 12, 14, 31, 48]
    # for index in arr:
    #     s.insert(index)
    # s.print_tree()


    tree = binaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.left = TreeNode(6)
    tree.root.right.right = TreeNode(7)
    tree.print_tree()


