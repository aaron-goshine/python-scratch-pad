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


