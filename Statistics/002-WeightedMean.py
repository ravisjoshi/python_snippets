"""
Input: [10, 40, 30, 50, 20] / [1, 2, 3, 4, 5]
Output: 32.0
"""

class weighted_mean_class:
    def weighted_mean(self, arr, weight_list):
        _sum = 0
        for index in range(len(arr)):
            _sum += arr[index]*weight_list[index]

        return _sum/sum(weight_list)

if __name__ == '__main__':
    obj = weighted_mean_class()
    arr = [10, 40, 30, 50, 20]
    weight_list = [1, 2, 3, 4, 5]
    print("{:.1f}".format(obj.weighted_mean(arr, weight_list)))

