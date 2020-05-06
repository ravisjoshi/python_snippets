"""
Input: aba / 10
Output: 7
abaabaabaa
~~~~~~~~~~
Input: a / 1000000000000
Output: 1000000000000
"""
#!/bin/python3

## Count number of 'a' in a repeated string
def repeatedString(s, n):
    first_count = rest_count = 0
    full_count = n // len(s)
    remaining_characters = n - (len(s) * full_count)

    for char in s:
        if char == 'a':
            first_count += 1
    for char in s[:remaining_characters]:
        if char == 'a':
            rest_count += 1

    count = first_count* full_count + rest_count

    return count

if __name__ == '__main__':

    s = input('Enter string to repeat:- ')
    n = int(input('Enter length of string:- '))

    print(repeatedString(s, n))
