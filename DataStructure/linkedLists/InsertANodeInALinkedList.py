"""
1) Insert a node at head
2) Insert a node at tail
3) Insert a node at a specified position
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def iamhead(self):
        if not self.head:
            return None
        else:
            return self.head

    def print_list(self):
        if not self.head:
            print('No element in linked-list!!!')
        else:
            cur_node = self.head
            while cur_node.next:
                print(cur_node.data, end=' -> ')
                cur_node = cur_node.next
            print(cur_node.data)

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = Node(data)

    def insertNodeAtPosition(self, head, data, position):
        if position == 0:
            new_node = Node(data)
            new_node.next = head
            return new_node
        else:
            cur_node = head
            new_node = Node(data)
            count = 0
            while count < position-1:
                cur_node = cur_node.next
                count += 1
            temp = cur_node.next
            cur_node.next = new_node
            new_node.next = temp
        return head

    def insertNodeAtHead(self, head, data):
        new_node = Node(data)
        new_node.next = head
        self.head = new_node
        return new_node

    def insertNodeAtTail(self, head, data):
        if not head:
            head = Node(data)
        else:
            cur_node = head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = Node(data)
        return head

if __name__ == '__main__':
    obj = SinglyLinkedList()
    list_elements = [1, 1, 2, 3, 3]
    for element in list_elements:
        obj.insert(element)

    # Print linked List
    obj.print_list()

    # Enter new data in linked list
    data = int(input('What data you want to insert in linked List:- '))
    position = int(input('At what position do you want it:- '))
    headOfLinkedList = obj.insertNodeAtPosition(obj.iamhead(), data, position)

    # Print linked List
    print('Updated linked list - after inserting above data:')
    obj.print_list()

    # Enter new node at head of linked list
    data = int(input('What data you want to insert at head of linked List:- '))
    newHeadOfLinkedList = obj.insertNodeAtHead(obj.iamhead(), data)

    # Print linked List
    print('Updated linked list - after inserting above data:')
    obj.print_list()

    # Append node at tail of linked list
    data = int(input('What data you want to append in linked List:- '))
    oneMoreHeadOfLinkedList = obj.insertNodeAtTail(obj.iamhead(), data)

    # Print linked List
    print('Updated linked list - after appending above data:')
    obj.print_list()


