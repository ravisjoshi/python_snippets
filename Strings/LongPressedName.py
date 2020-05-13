"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Input: name = "alex", typed = "aaleex"   /   Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Input: name = "saeed", typed = "ssaaedd"   /   Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Input: name = "leelee", typed = "lleeelee"   /   Output: true
Input: name = "laiden", typed = "laiden"   /   Output: true
Explanation: It's not necessary to long press any character.
Constraints:
    1 <= name.length <= 1000
    1 <= typed.length <= 1000
    The characters of name and typed are lowercase letters.
"""
import itertools

class Solution:
    def isLongPressedName(self, name, typed):
        if name == typed:
            return True
        d1 = [(k1, len(list(grp))) for k1, grp in itertools.groupby(name)]
        d2 = [(k2, len(list(grp))) for k2, grp in itertools.groupby(typed)]
        if len(d1) != len(d2):
            return False
        return all(k1 == k2 and v1 <= v2 for (k1,v1), (k2,v2) in zip(d1, d2))

    def isLongPressedName_method2(self, name, typed):
        if name == typed:
            return True
        if not (name[0] == typed[0] and name[-1] == typed[-1]):
            return False

        first = second = 0
        prev = ''

        for _ in range(len(typed)):
            while first < len(name):
                if name[first] == typed[second] and first < len(name):
                    prev = name[first]
                    first += 1
                    second += 1
                    break
                if prev == typed[second]:
                    second += 1
                    break
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    name = "alex"
    typed = "aaleex"
    print(s.isLongPressedName(name, typed))  # True

    name = "saeed"
    typed = "ssaaedd"
    print(s.isLongPressedName(name, typed))  # False

    name = "vtkgn"
    typed = "vttkgnn"
    print(s.isLongPressedName(name, typed))  # True

    name = "znxnorutzt"
    typed = "zznxxnnooruuzztt"
    print(s.isLongPressedName(name, typed))  # False

