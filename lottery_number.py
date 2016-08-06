##
# Compute the random distinct numbers for a lottery ticket
#
from random import randrange

MIN = 1
MAX = 49
NUMS = 6

# Keep a list of the numbers for the ticket
ticket_nums = []

# General NUM_NUMS random but distinct
for i in range(NUMS):
    #  Generate a number that isn't already on the ticket
    rand = randrange(MIN, MAX + 1)
    while rand in ticket_nums:
        rand = randrange(MIN, MAX + 1)
    # Add the distinct number to the ticket
    ticket_nums.append(rand)

# Sort the number into ascending order and display them
ticket_nums.sort()
print("Your number are: " , end="")
print(ticket_nums)

