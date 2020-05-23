#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def iamhead(self):
        if self.head:
            return self.head

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


    def print_doubly_linked_list(self, node):
        cur_node = node
        while cur_node:
            print(cur_node.data, end=' <-> ')
            cur_node = cur_node.next

    def sortedInsert(self, head, data):
        if head:
            cur_node = head
            new_node = DoublyLinkedListNode(data)

            # Insert at start
            if data < cur_node.data or data == cur_node.data:
                new_node.next = cur_node
                cur_node.prev = new_node
                return new_node

            # Insert in middle/end
            while cur_node.next and data >= cur_node.data:
                cur_node = cur_node.next
            if data < cur_node.data:
                cur_node.prev.next = new_node
                new_node.prev = cur_node.prev
                new_node.next = cur_node
            else:
                cur_node.next = new_node
                new_node.prev = cur_node
        return head


if __name__ == '__main__':
    llist = DoublyLinkedList()

    llist_count = int(input('How many elements you want to insert in dll:- '))
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    # Print DLL
    llist.print_doubly_linked_list(llist.iamhead())

    # Insert new data in DLL
    data = int(input('\nWhat data you want to insert in above dll:- '))
    llist1 = llist.sortedInsert(llist.head, data)

    # Print DLL
    llist.print_doubly_linked_list(llist1)

