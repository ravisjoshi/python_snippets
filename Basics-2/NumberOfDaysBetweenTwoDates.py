"""
Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Input: date1 = "2019-06-29", date2 = "2019-06-30"  /  Output: 1
Input: date1 = "2020-01-15", date2 = "2019-12-31"  /  Output: 15

Constraints: The given dates are valid dates between the years 1971 and 2100.
"""

from datetime import date
class Solution:
    def daysBetweenDates(self, date1, date2):
        if date1 == date2:
            return 0
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        d1 = date(y1, m1, d1)
        d2 = date(y2, m2, d2)
        delta = d2 - d1
        return abs(delta.days)

s = Solution()
date1 = "2019-06-29"
date2 = "2019-06-30"
print(s.daysBetweenDates(date1, date2))
