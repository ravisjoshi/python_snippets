"""

"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList():
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

    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

ll = linkedList()
ll.append("Ravi")
# ll.printList()
ll.append("Shankar")
# ll.printList()
ll.append("Joshi")
ll.printList()