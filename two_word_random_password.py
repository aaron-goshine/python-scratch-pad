##
# Generate a password by Concatenating two random words.
# The password will be between 8 and characters, and each word
# will be at least three letters long.
#

from random import randrange

WORD_FILE = "/usr/share/dict/words"

# Read all of the words from the files,
# only keeping those that are between 3 and 7
# characters in length, and store them in a list
#
words = []
inf = open(WORD_FILE, "r")
for line in inf:
    # Remove the newline character
    line = line.rstrip()

    # Keep words that are between 3 and 7 letters long
    if len(line) >= 3 and len(line) <= 7:
        words.append(line)

# Close the file
inf.close()

# Randomly select the first word for
# the password. It can be any word.
first = words[randrange(0, len(words))]
first = first.capitalize()

# Keep selecting a second word until we fine one
# that doesn't make the password too long
password = first
while len(password) < 8 or len(password) > 10:
    second = words[randrange(0, len(words))]
    second = second.capitalize()
    password = first + second

# Display the generated password
print("The random password is:", password)



