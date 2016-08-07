##
# Tokenizing a string containing a  expression
#

# Convert a mathematical expression into a list tokens
# @param s the string to tokenize
# @return a list of the tokens in s, or empty list if an
# error occurs
def tokenList (s):
    # Remove all of the spaces from s
    s = s.replace(" ", "")
    # Loop through all of the characters in the string
    # identifying the token and adding then to the list
    tokens = []
    i = 0
    while i < len(s):
        # Handle the token that are always a single character: *, /, ^, (and)
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or s[i] == "(" or s[i] == ")":
            tokens.append(s[i])
            i = i + 1

        # Handle + and -
        elif s[i] == "+" or s[i] == "-":
            # if there is a previous character and it is a number or close
            # bracket then the +  or - is a token on its own
            if i > 0 and (s[i - 1] >= "0" and s[i - 1] <= "9" or s[i - 1] == ")"):
                tokens.append(s[i])
                i = i + 1
            else:
                # The + or - is part of a number
                num = s[i]
                i = i + 1

                # Keep on adding characters to the token as long as they are digits
                while i < len(s) and s[i] >= "0" and s[i] <= "9":
                    num = num + s[i]
                    i = i + 1
                tokens.append(num)

        # Handle a number without a leading + and -
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            # Keep on adding characters to the token as long as they are digits
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num + s[i]
                i = i + 1
            tokens.append(num)
        # Any other character means that the expression is not valid
        # Return an empty list to indicate that an error occurred
        else:
            return []
    return tokens

# Read an expression from the user and tokenize it, displaying the result
def main ():
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print("The tokens are: ", tokens)

# Call the main function only if the file has not been imported
if __name__ == "__main__":
    main()








