"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def isPalindrom(num):
    check_num = num
    if num == 1:
        return True
    count, reverted_num = 0, 0
    while num >= 1:
        remainder = num % 10
        num //= 10
        reverted_num = reverted_num*10 + remainder
        count += 1
    return check_num == reverted_num

def largestPalindrom(num):
    result_list = []

    for index in range(999, 1, -1):
        first = second = index
        while first > 1:
            if isPalindrom(first*second):
                # print('first: {} second: {}'.format(first, second))
                result_list.append(first*second)
            first -= 1
    print(result_list)
    return max(result_list)


num = 999
print(largestPalindrom(num))
