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
print("The tax is %.2f and the tip is %.2f, making the total %.2f" % (tax, tip, total))

##
# Compute the sum n positive integers.
#

# Read input from the user
n = int(input("Enter a positive integer: "))

# Compute the sum
sum = n * (n + 1) / 2

# Display the result
print("The sum first ", n, "positive integers is", sum)

##
# Demonstrate Python's mathematical operators and its math module.
#
from math import log10

# Read input values from user
a = int(input("Enter the integer value of a:"))
b = int(input("Enter the integer value of b:"))

# Compute and display the sum, difference, product,
# quotient and remainder
print(a, "+ ", b, "is ", a + b)
print(a, "- ", b, "is ", a - b)
print(a, "* ", b, "is ", a * b)
print(a, "/ ", b, "is ", a / b)
print(a, "% ", b, "is ", a % b)

# Compute the logarithm and the power
print("The base 10 logarithm of ", a, "is", log10(a))

##
# Compute the minimum collection of coins needed toe represent a number of cents
#
CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

# Read the number of cents from the user
cents = int(input("Enter the number of cents: "))
# Determine the number of toonies by performing an integer devision by 200.
# Then compute the amount of change that still needs to be considered by
# computing the remainder after dividing by 200.
print(" ", cents // CENTS_PER_TOONIE, "toonies")
cents = cents % CENTS_PER_TOONIE

# Repeat the process for loonies, dimes, and nickels
print(" ", cents // CENTS_PER_LOONIE, "loonies")
cents = cents % CENTS_PER_LOONIE

print(" ", cents // CENTS_PER_QUARTER, "quarters")
cents = cents % CENTS_PER_QUARTER

print(" ", cents // CENTS_PER_DIME, "dimes")
cents = cents % CENTS_PER_DIME

print(" ", cents // CENTS_PER_NICKEL, "nickels")
cents = cents % CENTS_PER_NICKEL

# Display the number pennies
print(" ", cents, "pennies")

##
# Convert height from feet and inches to centimeters
#
IN_PER_FT = 12
CM_PER_IN = 2.54

# Read input form the user
print("Enter your height: ")
feet = int(input(" Number of feet: "))
inches = int(input(" Number of inches: "))

# Compute the equivalent number of centimeters
cm = (feet * IN_PER_FT + inches) * CM_PER_IN
# Display the result
print("Your height in centimeters is: ", cm)

##
# Compute the amount of energy need to heat a volume of
# water, and the cost doing so.
#

# Define constant for the specific heat capacity of
# water and the price of electricity
WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWH = 2.777e-7

# Read the volume from the user
volume = float(input("Enter the amount of water in Milliliteres: "))
d_temp = float(input("Enter the temperature increase (degrees Celsius): "))

# Compute the energy in Joules
q = volume * d_temp * WATER_HEAT_CAPACITY

# Display the result in Joules
print("That will require %d Joules of energy." %q)

# Compute the cost
kwh = q * J_TO_KWH
cost = kwh * ELECTRICITY_PRICE

# Display the cost
print("That much energy will cost %.2f cents." % cost)

