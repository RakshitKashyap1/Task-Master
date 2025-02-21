# A program that sorts a list of numbers in ascending or descending order.

# Get user input for numbers
numbers = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of floats
number_list = [float(num) for num in numbers.split()]

# Get user input for sorting order
order = input("Sort in ascending (A) or descending (D) order? (A/D): ").strip().upper()

# Sort the list based on user choice
if order == 'A':
    sorted_list = sorted(number_list)
    print("Sorted list in ascending order:", sorted_list)
elif order == 'D':
    sorted_list = sorted(number_list, reverse=True)
    print("Sorted list in descending order:", sorted_list)
else:
    print("Invalid choice. Please enter 'A' for ascending or 'D' for descending.")