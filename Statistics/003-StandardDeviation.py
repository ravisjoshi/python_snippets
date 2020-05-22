"""
1) Calculate the Mean (the simple average of the numbers)
2. Then for each number: subtract the Mean and square the result
3. Then work out the mean of those squared differences.
4. Take the square root of that and we are done!
"""
from math import sqrt

def stdDeviation(arr):
    mean = sum(arr)/len(arr)
    square_list = []
    for num in arr:
        x = mean-num
        square_list.append(x*x)
    sq_mean = sum(square_list)/len(square_list)
    return sqrt(sq_mean)


# arr = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]
arr = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]

print('{:.1f}'.format(stdDeviation(arr)))
