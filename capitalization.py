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


