#-----------#-------------

def harmonic (n):
    #Compute the sum of 1/k for k = 1 to n
    total = 0.0
    for k in range (1, n + 1):
        total += 1.0 / k
    return total

def _main ():
    n = int (input("Enter a positive integer "))
    print ("The sum of 1/k for k = 1 to ", n , "is", harmonic(n))

_main()

