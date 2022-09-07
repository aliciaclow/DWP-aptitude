#This is a recursive function to find the factorial of an integer
def factorial(x):

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))

# take input from the user
num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)