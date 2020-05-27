"""
A closure is a nested function which has access to a free variable from an enclosing function that has finished its execution. Three characteristics of a Python closure are:
    1) it is a nested function
    2) it has access to a free variable in outer scope
    3) it is returned from the enclosing function
A free variable is a variable that is not bound in the local scope. In order for closures to work with immutable variables such as numbers and strings, we have to use the nonlocal keyword.
Python closures help avoiding the usage of global values and provide some form of data hiding. They are used in Python decorators.
"""

def outer_function(text):
    greeting = text
    def inner_function(name):
        print('{}, {}'.format(greeting, name))
    # We are returning inner_function, without executing it - so no ()
    return inner_function

hi_function = outer_function('Hi')
hello_function = outer_function('Hello')

# Now it's time to call the function
hi_function('Ravi')
hello_function('Joshi')
