##
# Reduce an imperial measurement so that it is expressed using
# the largest possible unit of measure. For example, 59 teaspoon
# to 1 cup...
#

TSP_PER_TBSP = 3
TSP_PER_CUP = 48

## Reduce an imperial measurement to that it is expressed using
# the largest unit of measure.
# @param num the number of units that need to be reduced
# @param unit the unit of measure (cup, tablespoon or teaspoon)
# @return a string representing the measurement in reduce form
def reduceMeasure (num, unit):
    # Compute the number of teaspoons that the parameters represent
    unit = unit.lower()
    if unit == "teaspoon" or unit == "teaspoons":
        teaspoons = num
    elif unit == "tablespoon" or unit == "tablespoons":
        teaspoons = num * TSP_PER_TBSP
    elif unit == "cup" or unit == "cups":
        teaspoons = num * TSP_PER_CUP

    # Convert the number of teaspoon to largest possible units of measure
    cups = teaspoons // TSP_PER_CUP
    teaspoons = teaspoons - cups * TSP_PER_TBSP
    tablespoons = teaspoons // TSP_PER_TBSP
    teaspoons = teaspoons - tablespoons * TSP_PER_TBSP

    # Generate the result string
    result = ""

    # Add the number of cups to the result string (if any)
    if cups > 0 :
        result = result + str(cups) + " cup"
        # Make cup plural if there is  more that one
        if cups > 1:
            result = result + "s "

    # Add the number of tablespoon to the result sting (if any)
    if tablespoons > 0:
        if result != "":
            result = result + "s "

        result = result + str(tablespoons) + " tablespoon"
        # Make tablespoon plural if there is more than one
        if tablespoons > 1:
            result = result + "s "

    # Add the number of teaspoon to the result sting (if any)
    if teaspoons > 0:
        if result != "":
            result = result + "s "

        result = result + str(teaspoons) + " teaspoon"
        # Make teaspoon plural if there is more than one
        if teaspoons > 1:
            result = result + "s "

    # Handle the case where the number of units was 0
    if result == "":
        result = "0 teaspoon "

    return result


# Demonstrate the reduce measure function by preforming several reductions

def main ():
    print("59 teaspoons is %s." % reduceMeasure(59, "teaspoon"))
    print("59 tablespoons is %s." % reduceMeasure(59, "tablespoon"))
    print("99 teaspoons is %s." % reduceMeasure(99, "teaspoon"))

main()





