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
    print ("===========================================")
    print ("On the", intToOrdinal(n), "day of Christmas")
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
        print("A"),
    else:
        print("And a", end= "")
        print("Partridge in a tree.")

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


##
# Improve the capitalization of a string by replacing "i" with "I" and by
# capitalizing the first letter of each sentence.
#

## Capitalize the appropriate characters in the string
# @param s the string  that needs capitalization improved
def capitalize (s):
    # Correct the capitalization for i
    result = s.replace(" i ", " I ")

    # Capitalize the first character of the string
    if len(s) > 0:
        result = result[0].upper() + result[1: len(result)]

    # Capitalize the first letter that follow a ".", "!" or "?":
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            # Move past the ".", "!" or "?"
            pos = pos + 1

            # Move past any spaces
            while pos < len(s) and result[pos] == " ":
                pos = pos + 1

            # if we haven't reach the end of the string then replace
            # the current character with it's uppercase equivalent
            if pos < len(s):
                result = result[0 : pos] + \
                        result[pos].upper() + \
                        result[pos + 1 : len(result)]
        # Move to the next character
        pos = pos + 1

    return result

print(capitalize("this sentence is capitalize by python, yeah?"))

##
# Determine whether or not a string entered by the user is an integer?
#

## Determine if a string contains a valid representation of an integer
# @param s the string to check
# @return True ifs represent and integer. False otherwise
#
def isInteger (s):
    # Remove white space from the beginning and end of the string
    s = s.strip()

    # Determine if the remaining characters from a valid integer
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

print("Is `1121s` an integer", isInteger("1121s"))

##
# Determine whether or not a number is prime
#

## Determine whether or not a number is prime
# @prime n the integer to test
# @ return True if the number is prime, False otherwise
def isPrime(n):
    if n <= 1:
        return False

    # Check each number from 2 up to but not
    # including n to see if it divides evenly into n
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Is 1234567 a prime", isPrime(1234567))

##
# Generate and display a random password
#
from random import randint
SHORTEST = 8
LONGEST  = 12
MIN_ASCII = 33
MAX_ASCII = 126

## Generate a random password
# @return a string containing a random password
def randomPassword ():
    # Select a random length for the password
    randomLength = randint(SHORTEST, LONGEST)
    # Generate and appropriate number of random characters,
    # adding each one to the end of result
    result = ""
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result = result + randomChar
    # Return the random password
    return result

print("Your new password is: ", randomPassword())

##
# Check whether or not a password is good.
#

## Check whether or not a password is good.
# A good password is at lease 8 characters long
#  and contains an uppercase letter, a lowercase letter
#  and a number

def checkPassword(password):
    has_upper = False
    has_upper = False
    has_num = False

    # Check each character in the password and see
    # which requirement it meets
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True

    # If the password has all 4 properties
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True

# Demonstrate the password checking function
rnd_password = randomPassword()
print(rnd_password, "is valid", checkPassword(rnd_password))

##
# Convert a number from one base to another.
# Both the source base and the destination base must be
# between 2 and 16
#

# from hex_digit import *

def int2hex(number):
    hexstring = '' if number > 0 else '0'
    while number > 0:
        hexstring += '0123456789ABCDEF'[number % 16]
        number = int(number / 16)
    return hexstring[::-1]

def hex2int(string):
    return int(string, 16)

## Convert a number from base 10 to base n
# @param num the base 10 number to convert
# @param new_base the base to convert to
# @return the string of digit new_base
def dec2n (num, new_base):
    # Generate the representation of num in base new_base,
    # storing it in result
    result = ""
    q = num

    # Perform the body the body of the loop once
    r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

    # Continue looping until q == 0
    while q > 0:
        r = q % new_base
        result = int2hex(r) + result
        q = q // new_base

    # Return the result
    return result

## Convert a number from base b to base 10
# @param num the base b number, stored in a string
# @param b the base of the number to convert
# @return the base 10 number
def n2dec (num, b):
    decimal = 0
    power = 0

    # Process each digit in the base b number
    for i in range(len(num)):
        decimal = decimal * b
        decimal = decimal + hex2int(num[i])

    # Return the result
    return decimal

# Convert to base 10 and display the result
from_num = "10011100100"
from_base = 2
dec = n2dec(from_num, from_base)
print("That's %d in base 10." % dec)


# Convert to a new base and display the result
to_base = 64
to_num = dec2n(dec, to_base)
print("That's %s in base %d." % (to_num, to_base))


