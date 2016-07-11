##
# Display a person's complete mailing address.
#

print("Aaron Goshine")
print("Department of Computer Science")
print("University of Oxford")
print("University in Oxford, England")
print("UK")


##
# Compute the area of a room
#

#Read the input values from the user
length = float(input("Enter the length of the room in feet:"))
width  = float(input("Enter the width of the room in feet:"))

# Compute the area of the room
area = length * width

# Display the result
print("The area of the room is", area, "square feet")


##
# Compute the area of a field, reporting the result in acres.
#

SQFT_PER_ACRE = 42560

# Read input from the user
length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

# Compute the area in acres
acres = length * width / SQFT_PER_ACRE

# Display the result
print ("The area of the field is", acres, "acres")

##
# Compute the refund amount for a collection of bottles.
#
LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

# Read input from user
less = int(input("How many containers 1 litre or less do you? "))
more = int(input("How many containers more than 1 litre do you have? "))

# Compute the refund amount
refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT

# Display the result
print("Your total refund will be $%.2f." % refund)

##
# Compute the tax and tip for a restaurant meal.
#
TAX_RATE = 0.5
TIP_RATE = 0.18

# Read the cost of the meal for the user
cost = float(input("Enter the cost of the meal: "))

# Computer the tax and the tip
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip

# Display the result
print("The tax is %.2f and the tip is %.2f" % (tax, tip, total))


