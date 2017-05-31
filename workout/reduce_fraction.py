##
# Reduce a fraction to its lowest term.
#

## Compute the greatest common divisor of two integers.
# @param n the first integer under consideration (must be none-zero)
# @param m the second integer under consideration (must be non-zero)
# @return the greatest common divisor of the integers
def gcd (n, m):
    # Initialize d to the smallest of n and m
    d = min(n, m)

    #Use a while loop to find the greatest common divisor of n and m
    while n % d != 0 or m % d != 0:
        d = d - 1
    return d

## Reduce a fraction to lowest terms
# @param num the integer numerator of the fraction
# @param den the integer denominator or the fraction
# @return the numerator is 0 then the reduced fraction
def reduce (num, den):
    # If the numerator is 0 then the reduced fraction 0/1
    if num == 0:
        return (0, 1)
    # Compute the greatest common divisor of the numerator and
    # denominator
    g = gcd(num, den)

    # Divide both the numerator and denominator
    # by the gcd and return the result
    return (num // g, den // g)

# Read the fraction from the user and display the reduced fraction
def main ():
    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))

    # Compute the reduced fraction
    (n, d) = reduce(num, den)

    # Display the result
    print("%d/%d can be reduce to %d/%d." % (num, den, n, d))

# Call the main function
main()



