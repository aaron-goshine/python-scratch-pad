##
# Display all of the girls' and boys' names that were
# most popular in at least one year between 1900 and 2012
#
FIRST_YEAR = 1900
LAST_YEAR = 2012

## Load the first line from the file, extract the name, and
# add it the names list if it is not already present
# @param fname the name of the file to read the data from
# @param names the list to add the name to
# @return (None)
def LoadAndAdd(fname, name):
    # Open the file, read the first line, and extract the
    # names
    inf = open(fname, "r")
    line = inf.readline()
    inf.close()
    parts = line.split()
    name = parts[0]

    # Add the name to the list if it is not already present
    if name not in names:
        names.append(name)

# Display the girls and boys names that reached #1 in at least one
# year between 1900 and 2012
def main ():
    # Create two lists to store the most popular names
    girls = []
    boys = []

    # Process each year in the range, reading the first
    # lines from the files
    for year in range(FIRST_YEAR, LAST_YEAR + 1):
        girls_fname = "./data/" + str(year) + "_GirlsNames.txt"
        boys_fname = "./data/" + str(year) + "_BoysNames.txt"

        LoadAndAdd(girls_fname, girls)
        LoadAndAdd(boys_fname, boys)

    # Display the lists
    print("Girl' name that reached #1:")
    for name in girls:
        print(" ", name)
    print()
    print("Boys' names that reached #1: ")
    for name in boys:
        print(" ", name)

# Call the main function
main()

