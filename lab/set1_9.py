# A program that generates a multiplication table for a given number

# Get user input for the number
number = int(input("Enter a number to generate its multiplication table: "))

# Generate and display the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")