##
# Determine the proportion of words that of words that
# include each letter of the alphabet. The letter that is used
# in that is used in the smallest proportion of words is highlighted.
#


WORD_FILE = "/usr/share/dict/words"

# Maintain a dictionary that counts that number or
# words containing each letter
# Initialize the count for each letter to 0.

contains = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    contains[ch] = 0
# Open the file, and process each word, updating the
# contains dictionary
num_words = 0
inf = open(WORD_FILE, "r")
for word in inf:
    # Covert the word to uppercase the newline character
    word = word.upper().rstrip()

    # Before we can update the dictionary we need to generate a
    # list of unique letters in the word. Otherwise we will increase
    # the count multiple time for words that contains repeated
    # letter. We also to remove any hyphens that might be present.
    unique = []
    for ch in word:
        if ch not in unique and ch != "-" :
            unique.append(ch)
    # Now increment the counts for all the letter that are in the list of unique characters
    for ch in unique:
        contains[ch] = contains[ch] + 1

        # Keep count of the number of words that we have processed
        num_words = num_words + 1
# Close the file

# Display the result for each letter. While displaying the
# results we will also determine which character had the
# smallest count to that we can display it later.
smallest_count = min(contains.values())
smallest_letter = None
for ch in sorted(contains):
    if contains[ch] == smallest_count:
        smallest_letter = ch
    percentage = contains[ch] / num_words * 100
    print(ch, "occurs in %.2f percent of words" % percentage)
    # Display the letter that is easiest to avoid based on the
    # number of words in which it appears.
print()
print("The letter that is easiest to avoid is ", smallest_letter)


