##
# Compute the total due when several items are purchase.
# The amount payable for cash transaction is rounded to the closest nickel because
# pennies have been phased out.
#

PENNIES_PER_NICKEL = 5
NICKEL = 0.05

# Track the total of all the items
total = 0.00

# Read the price of the first item as a string
line = raw_input("Enter the price of the item (blank to quit): ")

# Continue reading items until a blank line is entered
while line != "":
    # Add the cost of the item to the
    # total (after convert it to a float
    total = total + float(line)

    # Read the cost of the next item
    line = raw_input("Enter the price of the item (blank to quit): ")

# Display the exact total payable
print("The exact amount payable is %.02f" % total)

# Compute the number or pennies that would be left it the
# total was paid only using nickels

rounding_indicator = total * 100 % PENNIES_PER_NICKEL

if rounding_indicator < PENNIES_PER_NICKEL / 2:
    # If the number of pennies left is less than 2.5
    # then we round down by subtracting that number of
    # pennies from the total
    cash_total = total - rounding_indicator / 100
else:
    # Otherwise we add a nickel and then subtract the
    # the number of pennies
    cash_total = total + NICKEL - rounding_indicator / 100


# Display the cash amount payable
print("The cash amount payable is %.02f" % cash_total)

