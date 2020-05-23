"""
Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.
"""

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def compare_lists(llist1, llist2):
    if not llist1 and not llist2:
        return 1
    elif not llist1 or not llist2:
        return 0
    else:
        node1 = llist1
        node2 = llist2
        while node1 and node2:
            if (node1.data != node2.data) or (node1.next and not node2.next) or (not node1.next and node2.next):
                return 0
            else:
                node1 = node1.next
                node2 = node2.next
    return 1


if __name__ == '__main__':
    llist1_count = int(input('How many elemements in LL1:- '))
    llist1 = SinglyLinkedList()
    for _ in range(llist1_count):
        llist1_item = int(input())
        llist1.insert_node(llist1_item)

    llist2_count = int(input('How many elemements in LL2:- '))
    llist2 = SinglyLinkedList()
    for _ in range(llist2_count):
        llist2_item = int(input())
        llist2.insert_node(llist2_item)

    print(compare_lists(llist1.head, llist2.head))

