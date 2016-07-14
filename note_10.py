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
    month == "September" or month == "November":
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

##
# Convert the name of a note to it's frequency
#
C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

# Read the note name from the user
name = input("Enter the two character not, such as C4: ")

# Store the note and its octave in s separate variable
note = name[0]
octave = int(name[1])

# Get the frequency of the note, assuming it is in the forth octave
if octave == 4:
    if note == "C":
        freq = C4_FREQ
    if note == "D":
        freq = D4_FREQ
    if note == "E":
        freq = E4_FREQ
    if note == "F":
        freq = F4_FREQ
    if note == "G":
        freq = G4_FREQ
    if note == "A":
        freq = A4_FREQ
    if note == "B":
        freq = B4_FREQ

# Now adjust the frequency to bring it into the correct octave
freq = freq / 2 ** (4 - octave)

# Display the result
print("The frequency of ", name, " is ", freq)

##
# Read frequency from the user and  display the
# note (if any) that it corresponds to.

LIMIT = 1

# Read the frequency from the user
freq = float(input("Enter a frequency: "))

# Determine the note that corresponds to the enter frequency.
# Set note equal to the empty string if there isn't a match.
if freq >= C4_FREQ - LIMIT and freq <= C4_FREQ + LIMIT:
    note = "C4"
elif freq >= D4_FREQ - LIMIT and freq <= D4_FREQ + LIMIT:
    note = "D4"
elif freq >= E4_FREQ - LIMIT and freq <= E4_FREQ + LIMIT:
    note = "E4"
elif freq >= F4_FREQ - LIMIT and freq <= F4_FREQ + LIMIT:
    note = "F4"
elif freq >= G4_FREQ - LIMIT and freq <= G4_FREQ + LIMIT:
    note = "G4"
elif freq >= A4_FREQ - LIMIT and freq <= A4_FREQ + LIMIT:
    note = "A4"
elif freq >= B4_FREQ - LIMIT and freq <= B4_FREQ + LIMIT:
    note = "B4"
else:
    note = ""

# Display the result, or and appropriate error message
if note == "":
    print("There is not note that corresponds to that frequeny.")
else:
    print("That frequency is ", note)

