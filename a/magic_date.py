##
# Determine all magic dates in the date range
#

days_in_month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if is_leap_year(year) and month == 2:
        return 29
    return days_in_month_list[month]

## Determine whether or not a date is "magic"
# @param day
# @param month
# @param year
# @return Boolean

def isMagicDate (day, month, year):
    if day * month == year % 100:
        return True
    return False

# Find and display all of the magic dates in the 1900s
def main ():
    for year in range(2000, 2100):
        for month in range(1, 13):
            for day in range(1, days_in_month(month, year) + 1):
                if isMagicDate(day, month, year):
                    print("%02d/ %02d/ %04d is a magic date." % (day, month, year))


main()

