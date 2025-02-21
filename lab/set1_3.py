#A program that generates a random password of a specified length

import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for the desired password length
length = int(input("Enter the desired password length: "))

# Generate and display the password
password = generate_password(length)
print(f"Generated password: {password}")