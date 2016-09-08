##
# Convert a number from Decimal to Binary
#

NEW_BASE = 2

# Read the number to convert
num = int(input("Enter a non-negative integer: "))

# Generate the binary representation of the num,
# storing it in result

result = ""
q = num

# Perform the body of the loop once
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE

# Keep on looping until q == 0
while q > 0:
    r = q % NEW_BASE
    result = str(r) + result
    q = q // NEW_BASE

# Display the result
print(num, "in Decimal", result, "in Binary.")
