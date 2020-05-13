"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
Now given a positive number N, how many numbers X from 1 to N are good?
Input: 10  /  Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note: N  will be in range [1, 10000].
"""
from time import sleep

class Solution:
    def rotatedDigits(self, num):
        count = 0
        rotate_dict = {0: '0', 1: '1', 2: '5', 5: '2', 6: '9', 8: '8', 9: '6'}
        for index in range(2, num+1):
            if '3' in str(index) or '4' in str(index) or '7' in str(index):
                continue
            sIndex, temp = str(index), ''
            for j in range(len(sIndex)):
                temp += rotate_dict[int(sIndex[j])]
                if j == len(str(index))-1 and int(temp) != index:
                    count += 1
        return count


    def rotatedDigits_method2(self, num):
        count = 0
        rotate_dict = {0: '0', 1: '1', 2: '5', 5: '2', 6: '9', 8: '8', 9: '6'}
        for index in range(2, num+1):
            sIndex, temp = str(index), ''
            for j in range(len(sIndex)):
                if int(sIndex[j]) not in rotate_dict.keys():
                    # print('{} not in {}'.format(str(index)[j], rotate_dict.keys()))
                    break
                temp += rotate_dict[int(sIndex[j])]
                if j == len(str(index))-1 and int(temp) != index:
                    count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    num = 10
    print(s.rotatedDigits(num))