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

##
# Generate and display one verse of the Twelve Days of Christmas
# @param n the verse to generate
# @return (none)
#
def displayVerse (n):
    print "==========================================="
    print "On the", intToOrdinal(n), "day of Christmas"
    print("my true love sent to me: ")
    if n >= 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a milking,")
    if n >= 7:
        print("Seven swans a swimming,")
    if n >= 6:
        print("Six geese a laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves,")
    if n == 1:
        print "A",
    else:
        print "And a",
        print "Partridge in a tree."

for verse in range(1, 13):
    displayVerse(verse)

##
# Center a string of characters within the terminal
#

WIDTH = 80

##
# Create a new string that will be centered within
# a given width
# @param s the string that will be centered
# @param width the in which the string will be centered
# @return a new copy of s that contains the leading spaces needed
# so that s will appear centered when it is printed
#
def center(s, width):
    # if the string is too long to center,
    # then original string is return
    if width < len(s):
        return s
    # Compute the number of spaces needed and generate the result
    spaces = (width - len(s)) // 2
    result = " " * spaces + s

    return result

print(center("A Famous Story", WIDTH))

