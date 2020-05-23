"""
The first linked list is: 1 -> 2 -> 3 -> NULL
The second linked list is: 3 -> 4 -> NULL
Hence, the merged linked list is: 1 -> 2 -> 3 -> 3 -> 4 -> NULL
"""
class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None

    def iamhead(self):
        if not self.head:
            return None
        else:
            return self.head

    def print_list(self, head):
        if not head:
            print('No element in linked-list!!!')
        else:
            cur_node = head
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

    def mergeLists(self, head1, head2):
        if not head1 and not head2: return None
        elif not head1 and head2: return head2
        elif head1 and not head2: return head1

        if head1.data < head2.data:
            smallerNode = head1
            smallerNode.next = self.mergeLists(head1.next, head2)
        else:
            smallerNode = head2
            smallerNode.next = self.mergeLists(head1, head2.next)

        return smallerNode


if __name__ == '__main__':
    obj1 = singlyLinkedList()
    list1_elements = [1, 2, 3]
    for element in list1_elements:
        obj1.insert(element)

    obj2 = singlyLinkedList()
    list2_elements = [3, 4]
    for element in list2_elements:
        obj2.insert(element)

    # Print linked List
    print('Linked List-1: ', end=' ')
    obj1.print_list(obj1.iamhead())
    print('Linked List-2: ', end=' ')
    obj2.print_list(obj2.iamhead())

    # Merge above linked lists
    obj3 = singlyLinkedList()
    returnNode = obj3.mergeLists(obj1.iamhead(), obj2.iamhead())
    obj3.print_list(returnNode)

