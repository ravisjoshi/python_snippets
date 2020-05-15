"""
Given a Book class and a Solution class, write a MyBook class that does the following:
1 - Inherits from Book
2 - Has a parameterized constructor taking these parameters:
    * string title
    * string author
    * int price

Implements the Book class' abstract display() method so it prints these 3 lines:
Title: a space, and then the current instance's title
Author: a space, and then the current instance's author
Price: a space, and then the current instance's price

Note: Because these classes are being written in the same file, you must not use an access modifier (e.g. public) when declaring MyBook or your code will not execute.

Input: The following input from stdin is handled by the locked stub code in your editor:
The Alchemist
Paulo Coelho
248

Output: The following output is printed by your display() method:
Title: The Alchemist
Author: Paulo Coelho
Price: 248
"""

from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(self): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: " + title)
        print("Author: " + author)
        print("Price: " + str(price))


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
