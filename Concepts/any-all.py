# Use of any & all

stuff = [1, 2, 3, 4, 5]
if any(x > 2 for x in stuff):  # true for stuff
    print('one item in the list is > 2')

if all(x > 2 for x in stuff):  # false for stuff
    print('all items in the list are > 2')

