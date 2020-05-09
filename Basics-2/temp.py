class Solution:
    def reverseBits(self, num):
        output = 0
        exp = 31
        while num > 0:
            remainder = num % 2
            num = num // 2
            output += remainder*2**exp
            exp -= 1

        return output

if __name__ == '__main__':
    s = Solution()
    num = 10000
    print(s.reverseBits(num))
