#define conversion calculation function
def TimeConvert(num): 

    num = int(num)
    hours = num // 60
    minutes = num % 60
    return f'{hours}:{minutes}'

# take input from the user
num = int(input("Enter a number: "))

# shows result to screen
print(TimeConvert(num))