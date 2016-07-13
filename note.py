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

##
# Calculate the speed of an object when it hits the ground after
# being dropping
#
from math import sqrt

# Define a constant for the acceleration due to gravity in m/s**2
GRAVITY = 9.8

# Read the height form which the object is dropped
d = float(input("Height form which the object is dropped (in meters): "))

# Compute the final velocity
vf = sqrt(2 * GRAVITY * d)

# Display the result
print("It will hit the ground at %.2f m/s. " % vf)

##
# Compute the are of a regular polygon
#

from math import tan, pi

# Read input from the user
s = float(input("Enter the length of each side of the polygon: "))
n = int(input("Enter the number of sides: "))

# Compute the area of the polygon
area = (n * s ** 2) / (4 * tan(pi / n))

# Display the result
print("The area of the polygon is", area)

##
# Convert a number of seconds to days, hours, minutes and seconds
#
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

# Read input form the user
seconds = int(input("Enter a number of seconds: "))

# Compute the days, hours, minutes and seconds
days = seconds / SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY

hours = seconds / SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR

minutes = seconds / SECONDS_PER_MINUTE
seconds = seconds % SECONDS_PER_MINUTE

# Display the result with the desired formatting
print("The equivalent duration is",  "%d:%02d:%02d:%02d." % (days, hours, minutes, seconds))

##
# Compute the wind chill index for a given air temperature and wind speed
#
WC_OFFSET = 13.12
WC_FACTOR1 = 0.6215
WC_FACTOR2 = -11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16

# Read the air temperature and wind speed for the user
temp = float(input("Enter the air temperature (degrees Celsius): "))
speed = float(input("Enter thye wind speed (kilometers per hour): "))

# Compute the wind chill index
wci = WC_OFFSET + WC_FACTOR1 * temp + WC_FACTOR2 + speed ** WC_EXPONENT + \
        WC_FACTOR3 * temp * speed ** WC_EXPONENT

# Display the result rounded to the closest integer
print("The wind chill index is", round(wci))

##
# Sort 3 values entered by the user into increasing order
#

# Read the numbers from the user, naming them a, b and c
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

mn = min(a, b, c)
mx = max(a, b, c)
md = a + b + c - mn - mx

# Display the result
print("The numbers in sorted are: ")
print(" ", mn)
print(" ", md)
print(" ", mx)

##
# compute the price of a day old bread order
BREAD_PRICE = 3.49
DISCOUNT_RATE = 0.60

# Read the number of loaves from the user
num_loaves = int(input("Enter the number of  day old loaves: "))

# Compute the discount and total price
regular_price = num_loaves * BREAD_PRICE
discount = regular_price * DISCOUNT_RATE
total = regular_price - discount

# Display the result
print("Regular price:   %5.2f" % regular_price)
print("Discount:        %5.2f" % discount)
print("Total:           %5.2f" % total)

