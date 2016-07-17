##
# Determine whether or not a string is a palindrome.
#

# Read the input from the user
line = raw_input("Enter a string: ")

# Assume that the string is a palindrome until
# we can prove otherwise
is_palindrome = True

# Check the characters, starting from the end until
# the middle is reached

for i in range(0, len(line) // 2):
    # If the characters don't match then mark
    # the string as not a palindrome
    if line[i] != line[len(line) - i - 1]:
        is_palindrome = False

    # Display a meaningful out put message
    if is_palindrome:
        print(line, "is a palindrome")
    else:
        print(line, "is not a palindrome")


