##
# Compute the admission price for a group visiting the zoo
#

# Store the admission prices as constants
BABY_PRICE = 0.00
CHILD_PRICE = 16.00
ADULT_PRICE = 32.00
SENIOR_PRICE = 18.00

# Store the baby age limits as constants
BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

# Create a variable to hold the total
# admission cost for all guests
total = 0

# Keep on reading ages until the user enters a
# blank line
line = raw_input("Enter the age of the guest (blank to finish): ")
while line != "":
    age = int(line)

    # Add the correct amount to the total
    if age <= BABY_LIMIT:
        total = total + BABY_PRICE
    elif age <= CHILD_LIMIT:
        total = total + CHILD_LIMIT
    elif age <= ADULT_LIMIT:
        total = total + ADULT_PRICE
    else:
        total = total + SENIOR_PRICE

    # Read the  next line from the user
    line = raw_input("Enter the age of the guest (blank to finish): ")

# Display the total due for the group, formatted
# using two decimal places
print("The total for that group is $%.2f" % total)

