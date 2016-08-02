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


