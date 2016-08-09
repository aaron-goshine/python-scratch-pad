##
# Conduct a reverse lookup on dictionary, finding all of the keys that
# map to the provided value
#

## Conduct a reverse lookup on a dictionary
# @param data the dictionary to perform the reverse lookup
# @param value the value to  search for in the dictionary
# @return a list (possibly empty) o
def reverseLookup(data, value):
    # Construct a list of keys that map to the value
    keys = []

    for key in data:
        if data[key] == value:
            keys.append(key)

    return keys

def main ():
    # Dictionary

    frEn = {"le": "the", "la": "the", "livre": "book", "pomme": "apple"}
    print("The french words for 'the' are: ", reverseLookup(frEn, 'the'))

main()


