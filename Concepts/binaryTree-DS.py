class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if not cur_node.left:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if not cur_node.right:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print('Element already in tree!')

    def search(self, value):
        if self.root:
            return self._search(value, self.root)

    def _search(self, value, cur_node):
        if cur_node:
            if cur_node.value == value:
                return True
            else:
                if value < cur_node.value:
                    return self._search(value, cur_node.left)
                else:
                    return self._search(value, cur_node.right)
        return False

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node:
            self._print_tree(cur_node.left)
            print(cur_node.value)
            self._print_tree(cur_node.right)

    def height(self):
        if self.root:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if not cur_node:
            return cur_height
        else:
            left_height = self._height(cur_node.left, cur_height+1)
            right_height = self._height(cur_node.right, cur_height+1)

        return left_height if left_height > right_height else right_height

if __name__ == '__main__':
    obj = binary_search_tree()

    obj.insert(10)
    obj.insert(6)
    obj.insert(14)
    obj.insert(4)
    obj.insert(9)
    obj.insert(12)
    obj.insert(18)
    obj.insert(16)
    obj.insert(17)
    obj.insert(20)
    obj.insert(21)
    obj.insert(19)


    print('Tree height is: {}'.format(obj.height()))

    print(obj.search(19))


