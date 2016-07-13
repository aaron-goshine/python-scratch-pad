##
# Determine and display whether an integer by the user is event or odd
#

# Read the integer from the user
num = int(input("Enter an integer: "))

# Determine whether it is even or odd by using the
# modulus (reminder) operator

if num % 2 == 1:
    print(num, "is odd.")
else:
    print(num, "is even.")

##
# Determine if a letter is a vowel or a consonant.
#

# Read a letter from the user
letter = str(input("Enter a letter of the alphabet: "))

# Classify the letter and report the result
if  letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("It's a vowel")
elif letter == "y":
    print("Sometimes it's a vowel.. Sometime it's consonant.")
else:
    print("It's a consonant.")


##
# Report the name of a shape form its number of sides
#

# Read the number of sides from the user
nsides = int(input("Enter the number of sides: "))

# Determine the name, leaving it empty an unsupported
# number of side was entered.

name = ""
if nsides == 3:
    name = "triangle"
elif nsides == 4:
    name = "square"
elif nsides == 5:
    name = "pentagon"
elif nsides == 6:
    name = "hexagon"
elif nsides == 7:
    name = "heptagon"
elif nsides == 8:
    name = "octagon"
elif nsides == 9:
    name = "nonagon"
elif nsides == 10:
    name = "decagon"

# Display and error message of the name of the polygon
if name == "":
    print("That number of side is not supported by this program.")
else:
    print("That's a ", name)

##
# Display the number of days in a month.
#

# Read input from the user
month = input("Enter the name or a month")

#Compute the number days in the month
days = 31

if month == "April" or month == "June" or \
    month == "September" or mounth == "November":
    days = 30
elif month == "February":
    days = "28 or 29"

# Display the result
print(month, "has", days, "days in it.")

##
# Determine the name of a triangle from the length of its sides
#

# Read the side length from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Determine the triangle's name
if side1 == side2  and side2 == side3:
    name = "equilateral"
elif side1 == side2 or side2 == side3 or side3 == side1:
    name = "isosceles"
else:
    name = "scalene"

# Display the triangle's name
print("That's a", name, "triangle")


