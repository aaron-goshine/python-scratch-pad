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


