#A program that converts temperatures from Fahrenheit to Celsius and vice versa.

# Get user input for conversion type
choice = input("Convert from (F)ahrenheit or (C)elsius? (F/C): ").strip().upper()

if choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

elif choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9.0 / 5.0) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
else:
    print("Invalid choice. Please enter 'F' or 'C'.")