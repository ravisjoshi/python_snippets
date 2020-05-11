"""
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.
Input: "()"   /   Output: True
Input: "(*)"   /   Output: True
Input: "(*))"   /   Output: True
Input: ")("   /   Output: False
Input: "(((****))"   /   Output: True
"""
class Solution(object):
    def checkValidString(self, parenthesisString):
        leftP = rightP = 0
        for parenthesis in parenthesisString:
            leftP += 1 if parenthesis == '(' else -1
            rightP += 1 if parenthesis != ')' else -1
            if rightP < 0: break
            leftP = max(leftP, 0)

        return leftP == 0

if __name__ == '__main__':
    s = Solution()
    parenthesisString = "***)"
    print(s.checkValidString(parenthesisString))