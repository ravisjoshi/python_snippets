"""
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Input: day = 31, month = 8, year = 2019  /  Output: "Saturday"
Input: day = 18, month = 7, year = 1999  /  Output: "Sunday"
Input: day = 15, month = 8, year = 1993  /  Output: "Sunday"
Constraints: The given dates are valid dates between the years 1971 and 2100.
"""
from datetime import date

class Solution:
    def dayOfTheWeek(self, day, month, year):
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        w_day_dict = dict(zip(range(10), weekdays))
        d1 = date(year, month, day)
        wd = d1.weekday()
        return w_day_dict[wd]


s = Solution()
day = 31; month = 8; year = 2019
print(s.dayOfTheWeek(day, month, year))

day = 18; month = 7; year = 1999
print(s.dayOfTheWeek(day, month, year))