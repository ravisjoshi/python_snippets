"""
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input:-
{('sam', 99912222), ('tom', 11122222), ('harry', 12299933)}
['sam', 'edward', 'harry']

Output:-
sam=99912222
Not found
harry=12299933
"""

if __name__ == '__main__':
    num = int(input())
    name_numbers = [input().split() for _ in range(num)]
    phone_book = {k: v for k, v in name_numbers}
    while True:
        try:
            name = input()
            if name in phone_book:
                print('%s=%s' % (name, phone_book[name]))
            else:
                print('Not found')
        except:
            break
