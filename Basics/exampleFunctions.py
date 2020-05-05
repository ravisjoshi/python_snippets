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
    """ singleNumber:
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

    def is_happy(self, input_number, existing_values=set()):

        if input_number == 1:
            return True
        elif input_number in existing_values:
            return False
        else:
            existing_values.add(input_number)

        _square_sum = 0
        while input_number:

            remainder = input_number % 10
            input_number = input_number // 10
            _square_sum += remainder**2
            print("Remainder: {}, new input_number: {}".format(remainder, input_number))

        return self.is_happy(_square_sum, existing_values)

if __name__ == '__main__':
    s = Solution()
    h_num = 39
    print(s.isHappy(h_num))


