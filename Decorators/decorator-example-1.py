"""
With *args and **kwargs - we can pass any number of arguments or no arguments to the wrapper function
"""

def decorator_func(func):
    def wrapper_function(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_function

@decorator_func
def hello():
    print('I am noone')

@decorator_func
def hello_name(name):
    print('I am {}'.format(name))

@decorator_func
def hello_name_age(name, age):
    print('I am {} and my age is {}'.format(name, age))

hello()
hello_name('Ravi')
hello_name_age('Ravi', 30)
