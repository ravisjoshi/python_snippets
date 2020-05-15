"""
Reverse a singly linked list.
Input: 1->2->3->4->5->NULL   /   Output: 5->4->3->2->1->NULL
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def iamhead(self):
        if not self.head:
            return None
        else:
            return self.head

    def insert(self, head, value):
        self.head = head
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

    def reverseList(self, head):
        """
        1->2->3->4->5->NULL
        5->4->3->2->1->NULL
        """
        if not head:
            return head
        else:
            cur_node = head
            stack = ListNode()
            while cur_node.next:
                cur_node = cur_node.next




if __name__ == '__main__':
    obj = Solution()
    list_elements = [1, 1, 2, 2, 3, 3, 4, 5, 5]
    for element in list_elements:
        obj.insert(obj.iamhead(), element)

    # Print linked-list elements
    obj.print_list()

    # Deleting duplicates
    obj.reverseList(obj.iamhead())

    # Print linked-list elements
    obj.print_list()