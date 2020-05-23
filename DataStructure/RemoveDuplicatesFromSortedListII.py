"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.
Input: 1->2->3->3->4->4->5  /  Output: 1->2->5
Input: 1->1->1->2->3  /  Output: 2->3
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
            print('Empty linked list')
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

    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        cur = head
        toDel = None
        while cur != None:
            if cur.val == toDel:
                prev.next = cur.next
                cur = cur.next
            else:
                toDel = None
                if cur.next != None and cur.next.val == cur.val:
                    toDel = cur.val
                    prev.next = cur.next
                    cur = cur.next
                    continue
                prev.next = cur
                prev = cur
                cur = cur.next
        return dummyHead.next


if __name__ == '__main__':
    obj = Solution()
    list_elements = [1, 1, 2, 2, 3, 3, 4, 5, 5]
    for element in list_elements:
        obj.insert(element)

    # Print linked-list elements
    obj.print_list()

    # Deleting duplicates
    # obj.iamhead()
    obj.deleteDuplicates(obj.iamhead())

    # Print linked-list elements
    obj.print_list()