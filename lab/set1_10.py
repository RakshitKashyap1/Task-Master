# A program that converts a given number from one base to another.

def convert_base(number, from_base, to_base):
    # Convert the number from the source base to decimal
    decimal_number = int(number, from_base)
    
    # Convert the decimal number to the target base
    if to_base == 10:
        return str(decimal_number)
    elif to_base == 2:
        return bin(decimal_number)[2:]  # Remove '0b' prefix
    elif to_base == 8:
        return oct(decimal_number)[2:]  # Remove '0o' prefix
    elif to_base == 16:
        return hex(decimal_number)[2:].upper()  # Remove '0x' prefix and convert to uppercase
    else:
        return None

# Get user input for the number and bases
number = input("Enter the number to convert: ")
from_base = int(input("Enter the base of the given number (2, 8, 10, 16): "))
to_base = int(input("Enter the base to convert to (2, 8, 10, 16): "))

# Perform the conversion
converted_number = convert_base(number, from_base, to_base)

# Display the result
if converted_number is not None:
    print(f"{number} in base {from_base} is {converted_number} in base {to_base}.")
else:
    print("Invalid base entered. Please use 2, 8, 10, or 16.")