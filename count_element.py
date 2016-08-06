##
# Count the number of elements in a list are greater
# than or equal to some minimum value and less than some maximum value
#

# Determine how many elements in data are greater than or
# equal to min and less than max.
# @param data the list to process
# @param mn the minimum acceptable value
# @param mx the exclusive upper bond on acceptability
# @return the number of elements, e, such that mn <=, e < mx
def countRange (data, mn, mx):
    # Count the number of element within the acceptable range
    count = 0
    for e in data:
        # Check each element
        if mn <= e and e < mx:
            count = count + 1
    return count

def main ():
    data = range(1, 10)

    #Test a case where some element are within the range
    print("Count the elements in [1..10 that are between 5 and 7..")
    print("Result: %d Expected: 2" % countRange(data, 5, 7))

main()


