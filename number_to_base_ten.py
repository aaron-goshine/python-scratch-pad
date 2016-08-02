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


