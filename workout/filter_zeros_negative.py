##
# Read a collection of integers from the user. Display all of
# the negative numbers, followed by all zeros, followed by all
# positive numbers.
#

# Creative there lists to store negative, positive and zeros
negatives = []
zeros = []
positives = []

nums = []

# Read all of the integers from the user, storing each
# integer in the correct list

line = input("Enter an integer (blank to quit): ")
while line != "":
    num = int(line)
    nums.append(num)
    # Read the next line of input from the user
    line = input("Enter an integer (blank to quit): ")

for n in sorted(nums):
    print(n)
