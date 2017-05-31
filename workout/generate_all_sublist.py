##
# Compute all sub-lists of a list
#

## Generate a list of all the sub-lists of a list
# @param data the list for which the sub-lists are generated
# @return a list containing all of the sub-lists of data
def allSublists (data):
    # Start out with the empty list as the only sub-list of data
    sublists = [[]]

    # Generate all of the sub-lists of data from length 1 to len(data)
    for length in  range(1, len(data) + 1):
        # Generate the sub-lists starting at each index
        for i in range(0, len(data) - length + 1):
            # Add the current sub-list to the list of sub-lists
            sublists.append(data[i : i + length])

    return sublists

# Demonstrate the allSublists function
def main ():

    print("The sublists of [] are: ")
    print(allSublists([]))

    print("The sublists of [1] are: ")
    print(allSublists([1]))

    print("The sublists of [1, 2] are: ")
    print(allSublists([1, 2]))

    print("The sublists of [1, 2, 3] are: ")
    print(allSublists([1, 2, 3]))

    print("The sublists of [1, 2, 3, 4] are: ")
    print(allSublists([1, 2, 3, 4]))

main()
