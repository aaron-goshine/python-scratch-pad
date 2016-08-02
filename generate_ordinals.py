## Generate the ordinal for the given Int
def intToOrdinal (n):
    if n == 11 or n == 12 or n == 13:
        return str(n) + "th"
    elif n % 10 == 1:
        return str(n) + "st"
    elif n % 10 == 3:
        return str(n) + "rd"
    else:
        return str(n) + "th"

##
# Generate and display one verse of the Twelve Days of Christmas
# @param n the verse to generate
# @return (none)
#
def displayVerse (n):
    print ("===========================================")
    print ("On the", intToOrdinal(n), "day of Christmas")
    print("my true love sent to me: ")
    if n >= 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a milking,")
    if n >= 7:
        print("Seven swans a swimming,")
    if n >= 6:
        print("Six geese a laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves,")
    if n == 1:
        print("A"),
    else:
        print("And a", end= "")
        print("Partridge in a tree.")

for verse in range(1, 13):
    displayVerse(verse)


