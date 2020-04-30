"""
Doubly linked list
"""

class Node():
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None

class doublyLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        prev_node = self.head
        while prev_node.next:
            prev_node = prev_node.next
        prev_node.next = newNode
        newNode.prev = prev_node
        newNode.data = data

    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

dll = doublyLinkedList()
dll.append("Ravi")
dll.append("Joshi")
dll.append("A")
dll.append("B")
dll.append("X")
print(dll.printList())
