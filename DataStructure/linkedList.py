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

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Not in the list")
            return
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def insert_after_element(self, prev_element, data):
        cur_node = self.head
        while cur_node.data != prev_element:
            cur_node = cur_node.next
        new_node = Node(data)
        new_node.next = cur_node.next
        cur_node.next = new_node

    def delete_element(self, data):
        temp_Node = Node(data)
        if self.head.data == data:
            temp_Node = self.head.next
            self.head = temp_Node
            return
        cur_Node = self.head
        while cur_Node.next.data != data and cur_Node.next:
            cur_Node = cur_Node.next
        cur_Node.next = cur_Node.next.next

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
# ll.printList()
ll.insert_after_element('Shankar', 'Babbi')
ll.printList()
print('--------------')
ll.delete_element('Shankar')
ll.printList()
