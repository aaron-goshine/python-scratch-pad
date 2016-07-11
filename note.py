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

