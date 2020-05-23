"""
You are given a pointer to the root of a binary tree. Print the top view of the binary tree.
Top view means when you look the tree from the top the nodes, what you will see will be called the top view of the tree. See the example below.
You only have to complete the function.
For example :
   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Top View : 1 -> 2 -> 5 -> 6
Input Format: You are given a function,
void topView(node * root) {
}
Output Format: Print the values on a single line separated by space.
Input:
   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Output: 1 2 5 6
Explanation:
   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
From the top only nodes 1,2,5,6 will be visible.
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def topView(root):
    if root.left:
        printleftside(root.left)
    print(root.info)
    if root.right:
        printrightside(root.right)

def printleftside(node):
    if node:
        printleftside(node.left)
    else:
        return
    print(node.info)

def printrightside(node):
    if node:
        print(node.info)
        printrightside(node.right)
    else:
        return


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
