##
# Generate and display a random password
#
from random import randint
SHORTEST = 8
LONGEST  = 12
MIN_ASCII = 33
MAX_ASCII = 126

## Generate a random password
# @return a string containing a random password
def randomPassword ():
    # Select a random length for the password
    randomLength = randint(SHORTEST, LONGEST)
    # Generate and appropriate number of random characters,
    # adding each one to the end of result
    result = ""
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result = result + randomChar
    # Return the random password
    return result

print("Your new password is: ", randomPassword())

##
# Check whether or not a password is good.
#

## Check whether or not a password is good.
# A good password is at lease 8 characters long
#  and contains an uppercase letter, a lowercase letter
#  and a number

def checkPassword(password):
    has_upper = False
    has_upper = False
    has_num = False

    # Check each character in the password and see
    # which requirement it meets
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True

    # If the password has all 4 properties
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True

# Demonstrate the password checking function
rnd_password = randomPassword()
print(rnd_password, "is valid", checkPassword(rnd_password))


