"""
Use a stack data structure to convert integer values to binary
"""

class Stack():
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

s = Stack()

def int2binary(dec_num):
    while dec_num >= 1:
        s.push(str(dec_num % 2))
        dec_num //= 2
    convertedBinary = ""

    while not s.is_empty():
        convertedBinary += str(s.pop())
    return convertedBinary

num = int(input("Enter a number to convert to binary:-  "))

print(int2binary(num))
