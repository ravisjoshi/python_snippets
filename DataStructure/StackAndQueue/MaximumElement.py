"""
You have an empty sequence, and you will be given N queries. Each query is one of these three types:

1  -Push the element x into the stack.
2  -Delete the element present at the top of the stack.
3  -Print the maximum element in the stack.

Input Format: The first line of input contains an integer N. The next lines each contain an above mentioned query. (It is guaranteed that each query is valid.)
Output Format: For each type 3 query, print the maximum element in the stack on a new line.
Input:
How many queries you want to enter:-  10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3
Output:
26
91
"""

class stack_template:
    def __init__(self):
        self.myStack = []

    def insert_element(self, data):
        self.myStack.append(data)

    def delete_element(self):
        self.myStack.pop(-1)

    def find_max(self):
        return max(self.myStack)

if __name__ == '__main__':
    obj = stack_template()

    num_of_queries = int(input('How many queries you want to enter:- '))
    for _ in range(num_of_queries):
        temp = input('Enter out of 3 options:- ').split()
        if len(temp) == 2:
            # query_to_call = int(temp[0])
            # digit = int(temp[1])
            obj.insert_element(int(temp[1]))
        else:
            query_to_call = int(temp[0])
            if query_to_call == 2:
                obj.delete_element()
            else:
                print(obj.find_max())
