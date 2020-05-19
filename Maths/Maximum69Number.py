"""
Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Input: num = 9669  /  Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Input: num = 9996  /  Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Input: num = 9999  /  Output: 9999
Explanation: It is better not to apply any change.

Constraints:
    1 <= num <= 10^4
    num's digits are 6 or 9.
"""

class Solution:
    def maximum69Number(self, num):
        _str = str(num)
        arr = [s for s in _str]
        index = arr.index('6') if '6' in arr else None
        if index is not None:
            arr[index] = '9'
        return int("".join(arr))

    def maximum69Number_method2(self, num):
        return int(str(num).replace('6', '9', 1))


if __name__ == '__main__':
    s = Solution()
    num = 6699
    print(s.maximum69Number(num))

    num = 9669
    print(s.maximum69Number(num))

    num = 9999
    print(s.maximum69Number(num))

