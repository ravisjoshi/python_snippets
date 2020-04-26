"""
Given an expression string exp , write a program to examine whether the pairs and the
orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
{[]{()}} - Balanced
[{}{})(] - Unbalanced
((() - Unbalanced
"""
class checkParentheseseBalance():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


p = checkParentheseseBalance()
pString = '[{}{}()]'
for symbol in pString:
    if symbol in "[, {, (":
        p.push(symbol)
    elif p.is_empty() and symbol in "], }, )":
        print("Not Balanced!!")
        exit(0)
    elif symbol in "]" and p.peek() == '[':
        p.pop()
    elif symbol in "}" and p.peek() == '{':
        p.pop()
    elif symbol in ")" and p.peek() == '(':
        p.pop()
    else:
        p.push(symbol)

if p.is_empty():
    print("Evenly Balanced!!")
else:
    print("Not Balanced!!")