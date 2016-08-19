##
# Compute the total of a collection of numbers entered by the user.
# The user will enter a blank line to indicate that no further numbers
# will be entered
#

# Compute the total of all the numbers enter by the user
# @return the total
def readAndTotal():
    # Read a value from the user
    line = input("Enter a number (blank to quit): ")

    # Base case: The user entered a blank line so the total is 0
    if line == "":
        return 0
    else:
        # Recursive case: Convert the current line to a number
        # and use Recursive to read the next line
        return float(line) + readAndTotal()


##
# Determine whether or not a string is a palindrome
# @param s the string to check
# @return True is the string is palindrome, False otherwise
def isPalindrome (s):
    # Base case: the empty string is a palindrome only if  the first and last
    # characters are the same
    if len(s) <= 1:
        return True

    # Recursive case: The string is a palindrome only id the first
    # and last characters match, and the rest of the string is a
    # palindrome
    return s[0] == s[len(s) - 1] and isPalindrome(s[1 : len(s) - 1])

