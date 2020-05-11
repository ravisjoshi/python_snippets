class Solution:
    def fibonacci(self, num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        return (num * self.fibonacci(num -1))

if __name__ == '__main__':
    s = Solution()
    num = 5
    print(s.fibonacci(num))
