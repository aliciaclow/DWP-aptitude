# Python program to find the factorial of a number provided by the user
# using recursion

#USAGE: factorial.py '1-18'
import sys

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = int(sys.argv[1])

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)