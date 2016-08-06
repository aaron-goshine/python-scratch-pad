##
# Display a list of items that are separated by commas and
# the last word "and" appears between the final two items.
#

## Format a list of items so that they are separated by commas and  "and"
# @param items the list of items to format
# @return a sting containing the items with the desired formatting
#
def formatList(items):
    # Handle lists of items to format
    if len(items) == 0:
        return "<empty>"
    if len(items) == 1:
        return str(items[0])

    # Loop over all the item in the list except the last two
    result = ""
    for i in range(0, len(items) - 2):
        result =  result + str(items[i]) + ","

    # Add the second to last and last items to the
    # result list that contain numbers in addition
    # to separated by "and"

    result = result + str(items[len(items) - 2]) + " and "
    result = result + str(items[len(items) - 1])

    return result

def main ():
    # Read item from the user until a blank is entered
    items = []
    line = input("Enter an item (blank to quit): ")
    while line != "":
        items.append(line)
        line = input("Enter an item (blank to quite: ")

    # Format and display the items
    print("The items are %s, " % formatList(items))

main()
