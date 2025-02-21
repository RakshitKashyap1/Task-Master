# A program that checks if a given string is a palindrome

# Get user input for the string
input_string = input("Enter a string: ")

# Normalize the string: remove spaces and convert to lowercase
normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())

# Check if the string is a palindrome
if normalized_string == normalized_string[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')