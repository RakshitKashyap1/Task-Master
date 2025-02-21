#A program that calculates the factorial of a number.

# Get user input for the number
number = int(input("Enter a non-negative integer: "))

# Calculate the factorial
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is: {factorial}")