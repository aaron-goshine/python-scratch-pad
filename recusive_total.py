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

    # Read a collection of numbers from the user and display the total
def main():
    # Read the value from the user compute the total
    total = readAndTotal()

    # Display the result
    print("The total of all those values is", total)
main()

