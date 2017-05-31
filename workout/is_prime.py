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


