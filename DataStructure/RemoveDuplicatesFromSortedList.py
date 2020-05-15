"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
Input: 1->1->2  /  Output: 1->2
Input: 1->1->2->3->3  /  Output: 1->2->3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = ListNode(value)

    def print_list(self):
        if not self.head:
            print('No element in linked-list!!!')
        else:
            cur_node = self.head
            while cur_node.next:
                print(cur_node.val, end=' -> ')
                cur_node = cur_node.next
            print(cur_node.val)

    def deleteDuplicates(self):
        if not self.head:
            print('No entry in linked list!')
        else:
            cur_node = self.head
            while cur_node.next:
                if cur_node.val != cur_node.next.val:
                    cur_node = cur_node.next
                else:
                    cur_node.next = cur_node.next.next


if __name__ == '__main__':
    obj = Solution()
    list_elements = [1, 1, 2, 3, 3]
    for element in list_elements:
        obj.insert(element)

    # Print linked-list elements
    obj.print_list()

    # Deleting duplicates
    obj.deleteDuplicates()

    # Print linked-list elements
    obj.print_list()



