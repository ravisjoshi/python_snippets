"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
Input: 1   /   Output: "1"
Explanation: This is the base case.
Input: 4   /   Output: "1211"
"""

class Solution:
    def countAndSay(self, num):
        if num == 1:
            return '1'

        # Set the initial string
        output = '1'
        # Run the loop num-1 times
        for index in range(1, num):
            # We need to run this loop one extra time, so adding one dummy character
            output += '@'
            length = len(output)
            count = 1
            temp = ''
            for string_index in range(1, length):
                if output[string_index] == output[string_index-1]:
                    count += 1
                else:
                    temp += str(count)
                    temp += output[string_index-1]
                    count = 1
            output = temp

        return output

if __name__ == '__main__':
    s = Solution()
    num = 5
    print(s.countAndSay(num))

