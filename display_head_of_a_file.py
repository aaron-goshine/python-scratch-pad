##
# Display the head (first 10 lines) of a file whose name is
# provided as a command line parameter.
#

import sys
NUM_LINES = 10

# Verify that exactly one command line parameter was supplied
if len(sys.argv) != 2:
    print("You must provide the file name as a command line parameter.")
    quit()

try:
    # Open the file reading
    inf = open(sys.argv[1], "r")

    # Read the first line from the file
    line = inf.readline()

    # Keep looping until we either read and display 10 line or
    # we have reached the end of the file
    count = 0

    while count < NUM_LINES and line != "":
        # Remove the trailing newline character and count the line
        line = line.rstrip()
        count =  count + 1

        # Display the line
        print(line)

        # Read the next line from the file
        line = inf.readline()

    # Close the file
    inf.close();
except IOError:
     # Display a message if something goes
     # wrong while accessing the file
     print("An error has occurred while accessing the file.")


