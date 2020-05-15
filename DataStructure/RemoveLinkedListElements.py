"""
Remove all elements from a linked list of integers that have value val.
Input:  1->2->6->3->4->5->6, val = 6   /   Output: 1->2->3->4->5
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

    def removeElements(self, head, value):
        if not head:
            print('List is empty!')
        else:
            cur_node = head
            while cur_node:
                while cur_node.next and cur_node.next.val == value:
                    cur_node.next = cur_node.next.next
                cur_node = cur_node.next

            if head.val == value:
                head = head.next
        self.head = head
        return head

if __name__ == '__main__':
    obj = Solution()
    element_list = [1, 1, 2, 3, 3, 4, 5, 5]
    for element in element_list:
        obj.insert(element)

    obj.print_list()
    obj.removeElements(obj.iamhead(), 1)
    obj.print_list()

