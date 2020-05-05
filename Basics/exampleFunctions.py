from time import sleep

class Solution:
    """ removeElement:
    nums = [0, 1, 2, 2, 3, 0, 4, 2] & val = 2
    Output: [0, 1, 3, 0, 4]  OR  [0, 1, 3, 0, 4, 0, 4, 2]
    """
    def removeElement(self, nums, val):
        index = 0
        for i in range(len(nums)):
            if nums[i] == val:
                pass
            else:
                nums[index] = nums[i]
                index += 1
        return index
    """
    singleNumber: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    Input: [2,2,1]  /  Output: 1
    Input: [4,1,2,1,2]  /  Output: 4
    """
    def singleNumber(self, nums):
        _sum = 0
        for index, item in enumerate(nums):
            if index % 2 == 0:
                _sum += item
            else:
                _sum -= item

        return abs(_sum)
    """
    Input: 19  /  Output: true
    Explanation:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
    HappyNumber: Those numbers for which this process ends in 1 are happy numbers.
    """
    def isHappy(self, n):
        if n == 1:
            return True
        existing_value = set()
        _sum = 2
        while _sum > 1:
            _sum = 0
            for index, value in enumerate(str(n)):
                _sum += int(value)**2
            n = _sum
            print(_sum)
            sleep(1)
            if _sum == 1:
                return True
            elif _sum in existing_value:
                return False
            existing_value.add(_sum)

if __name__ == '__main__':
    s = Solution()
    h_num = 39
    print(s.isHappy(h_num))
