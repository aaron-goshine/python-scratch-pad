##
# Display a multiplication table fro 1 time 1 through 10 time 10
#

MIN = 1
MAX = 10

# Display the top now of labels
print("   ")
for i in range(MIN, MAX + 1):
    print("%4d" % i)
    print()

# Display the table
for i in range(MIN, MAX + 1):
    print("%4d" % i)
    for j in range(MIN, MAX + 1):
        print("%4d" % (i * j))
    print();

