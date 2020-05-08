"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0, None)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val,None)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val,None)
                l2 = l2.next
            cur = cur.next
        # outside loop whichever is left
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

if __name__ == '__main__':
    # l1 = [1, 2, 4]
    # l2 = [1, 3, 4]

    s = Solution()
    print(s.mergeTwoLists(l1, l2))
