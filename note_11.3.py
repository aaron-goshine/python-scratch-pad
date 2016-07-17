##
# Compute even parity for sets of 8 bits entered by the user
#
# Read the first line of input
line = raw_input("Enter 8 bit: ")

# Continue looping until a blank line is entered
while line != "":
    # Ensure that the line is a total of 8 zeros and exactly 8 character
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        # Display and appropriate error message
        print("That was not 8 bits. Try again.")
    else:
        # Count the number of ones
        ones = line.count("1")

        # Display the parity bit
        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")

    # Read the next line of input
    line = raw_input("Enter 8 bit: ")

