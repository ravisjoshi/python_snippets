"""
Mean: The "average" number; found by adding all data points and dividing by the number of data points.
Median: The middle number; found by ordering all data points and picking out the one in the middle (or if there are two middle numbers, taking the mean of those two numbers).
Mode: The most frequent number—that is, the number that occurs the highest number of times.
"""

class mmm:
    def calculate_mean(self, arr):
        return sum(arr)/len(arr)

    def calculate_median(self, arr):
        _len = len(arr)
        s_arr = sorted(arr)
        if _len % 2 != 0:
            return s_arr[_len//2]
        else:
            return (s_arr[_len//2]+s_arr[_len//2-1])/2

    def calculate_mode(self, arr):
        s_arr = set(arr)
        if len(s_arr) == 1:
            return min(s_arr)
        else:
            temp = {}
            i_am_max = []
            for num in s_arr:
                temp.update({num: arr.count(num)})
            max_count = max(temp.values())
            for j in temp.keys():
                if temp[j] == max_count:
                    i_am_max.append(j)
            return min(i_am_max)

if __name__ == '__main__':
    s = mmm()
    arr = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
    print(s.calculate_mean(arr))
    print(s.calculate_median(arr))
    print(s.calculate_mode(arr))
