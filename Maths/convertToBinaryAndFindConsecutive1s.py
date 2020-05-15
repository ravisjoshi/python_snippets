"""
Given a base-10 integer n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
Input: 5  /  Output: 1
Input: 13  /  Output 2

Explanation
Case 1: The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.
Case 2: The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.
"""

def countNoOfOnesinBinary(num):
    count = 0
    count_list = []
    while num >= 1:
        remainder = num % 2
        num //= 2
        count = count+1 if remainder == 1 else 0
        count_list.append(count)
    return max(count_list)

if __name__ == '__main__':
    num = int(input())
    print(countNoOfOnesinBinary(num))


