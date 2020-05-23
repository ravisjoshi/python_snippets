# https://www.youtube.com/watch?v=lVFnq4zbs-g&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV

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
s.push("Ravi")
s.push("Shankar")
print(s.get_stack())
s.pop()
print(s.get_stack())
s.push("Joshi")
print(s.peek())
print(s.get_stack())
print(s.is_empty())