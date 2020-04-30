"""
s = UDDDUDUUDUDDUDUU
Output: 3
s = UDDDUDUUDUDDUDUUDD
Output: 3
s = UDDDUDUUDUDDUDUUDU
Output: 4
s = UDDDUDUU
Output: 1
_/\      _
   \    /
    \/\/
"""
#!/bin/python3

def countingValleys(s):
    result = vally = 0
    goingDown = 0
    for num in range(len(s)):
        if s[num] is 'U':
            result += 1
        elif s[num] is 'D':
            result -= 1
        if result <= -1:
            goingDown = 1
        elif goingDown ==1 and result == 0:
            vally += 1
            goingDown = 0

    return (vally)

if __name__ == '__main__':

    path_string = input('Enter what kind of steps are those(up or down):-  ')

    print(countingValleys(path_string))
