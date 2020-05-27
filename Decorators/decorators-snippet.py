"""
Decorator is a function, that takes another function as an argument, adds some kind of functionality and returns another function.
All of this without altering the source code of the original function.
"""

def decorator_function(func):
    def wrapper_function():
        return func()
    return wrapper_function

def original_function():
    print('I am running in old fashion')

my_func = decorator_function(original_function)
my_func()

"""
We can also write the above one as below:
"""

def decorator_func(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

@decorator_func
def hello():
    print('I am running in new fashion')

hello()
