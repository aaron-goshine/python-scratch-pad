##
# A number, n, is perfect number if the sum of the proper
# divisors of n is equal to n. This program display all of the
# perfect numbers between 1 and LIMIT.
#

LIMIT = 10000

def proper_divisors(n):
    divisors = []
    for x in range(1, (n + 1) // 2 + 1):
        if n % x == 0 and n != x:
            divisors.append(x)
    return divisors

## Determine whether or not a number is perfect. A number is perfect if the
# sum of its proper divisors is equal to the number itself.
# @param n the number to check for perfection
# @return True if the number is perfect, False otherwise
def isPerfect (n):
    # Compute the total of all of the divisors
    divisors = proper_divisors(n)
    total = sum(divisors)
    # Return the appropriate result
    if total == n:
        return True
    return False

# Display all perfect numbers between 1 and LIMIT
def main ():
    print("The perfect numbers between 1 and ", LIMIT, "are: ")
    for i in range(1, LIMIT):
        if isPerfect(i):
            print(" ", i)

main()

