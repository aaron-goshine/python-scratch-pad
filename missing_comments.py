##
# Find and display the names of Python functions that are not immediately
# preceded by a comment.
#

from sys import argv

# Verify that at least one file name has been provided as a command line
# parameter
if len(argv) == 1:
    print("At least one filename must be provided as a ", \
            "command line param.")
    print("Quiting..")
    quit()

# Process each file provided as a command line parameter
for fname in argv[1: len(argv)]:
    # Attempt to process the file
    try:
        inf = open(fname, "r")

        # As we move through the file we need to keep a copy
        # of the previous line so that we can check to see if it
        # starts with a comment character.
        # We also need to keep track of the line number within the file
        prev = " "
        lnum = 1

        # Check each line in the current file
        for line in inf:
            # If line is a function definition and the previous line is not a
            # comment
            if line.startswith("def ") and prev[0] != "#":
                # Find the first '(' on the line so that we know where
                # the function name ends
                bracket_pos = line.index("(")
                name = line[4: bracket_pos]

                # Display information about the
                # function that is missing its comment
                print("%s line %d: %s" % (fname, lnum, name))
                # Save the current line and update the line counter
                prev = line
                lnum = lnum + 1
        #Close the current file
        inf.close()
    except:
        print("A problem was encoutered with file  '%s'. " % fname)
        print("Moving on to the next file...")

