#A program that calculates the average of a list of numbers.

# Get user input for numbers
numbers = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of floats
number_list = [float(num) for num in numbers.split()]

# Calculate the average
if number_list:  # Check if the list is not empty
    average = sum(number_list) / len(number_list)
    print(f"The average is: {average}")
else:
    print("No numbers were entered.")