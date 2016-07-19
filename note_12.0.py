##
# Compute and display the median of three values entered
# by the user, This program includes tow implementations of the
# median function that demonstrate different techniques for
# computing the media of three values.
#

## Compute the median of three value using if statements
# @param `a` the first value
# @param `b` the second value
# @param `c` the third value
# @return the median of values a, b, and c
#

def median (a, b, c):
    if a < b and b < c or a > b and b < c:
        return b;
    elif b < a and a < c or b > a and a > c:
        return a;
    if c < a and b < c or c > a and b > c:
        return c


## Compute the median value using the min
# and max functions
# @param `a` the first value
# @param `b` the second value
# @param `c` the third value
# @return the median of values a, b, and c
#

def alternativeMedian(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

# Display the median of 3 values
print("The median value is : ", median(1, 2, 3))
print("The median value calculate using alternative: ", alternativeMedian(1, 2, 3))

## Generate the ordinal for the given Int
def intToOrdinal (n):
    if n == 11 or n == 12 or n == 13:
        return str(n) + "th"
    elif n % 10 == 1:
        return str(n) + "st"
    elif n % 10 == 3:
        return str(n) + "rd"
    else:
        return str(n) + "th"

