##
# Compute the sum of numbers entered by the user,
# ignoring non-numeric input
#

# Read the fist line of input form the user
line = input("Enter a number: ")
total = 0

# Keep reading until the user enter a blank line
while line != "":
    try:
        # Try and convert the line to a number
        num = float(line)
        # If the conversion succeed then add it to total and display it
        total = total + num
        print("The total is now", total)

    except ValueError:
        # Display an error message going on to read the next value
        print("That wasn't a number: ")

    # Read the next number
    line = input("Enter a number: ")

# Display the total
print("The grand total is", total)


