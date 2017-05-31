##
# Compute the number of unique characters in a string using
# a dictionary
#

# Read the string from the user
s = input("Enter a string: ")


# Add each character to a dictionary with a value to True.
# Once we are done the number of keys in the dictionary
# will be the number of unique characters in the sting
characters = {}
for ch in s:
    characters[ch] = True


print("That string contained", len(characters), "unique characters(s).")
