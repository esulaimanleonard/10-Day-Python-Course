# ==========================================
# SECTION 4: Type Conversion Magic
# ==========================================

print("SECTION 4: Converting Between Types")
print("-" * 34)

# Exercise 4.1: String to Number for Calculations
# Learn to convert user input for math operations
print("🧮 Multi-Operation Calculator")

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

# Convert strings to numbers for math
num1 = int(first_number)
num2 = int(second_number)

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")


print("\n" + "="*50)

# YOUR CODE HERE - Create an operation selector:
# Ask for two numbers and which operation to perform
# YOUR CODE HERE:
# 🧮 Multi-Operation Calculator

# First section: perform all 3 basic operations
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

num1 = int(first_number)
num2 = int(second_number)

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")

print("\n" + "="*50)

# Second section: perform a chosen operation (still no logic)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

# Just print all results – no condition, user chooses visually
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")



print("\n" + "="*50)

# Exercise 4.2: Working with Decimals and Precision
# Learn about float conversion for precise calculations
print("\n💰 Financial Calculator")

price = input("Enter the price: $")
tax_rate = input("Enter tax rate (like 0.08 for 8%): ")
tip_percentage = input("Enter tip percentage (like 0.15 for 15%): ")

# Convert to floats for decimal calculations
price_float = float(price)
tax_float = float(tax_rate)
tip_float = float(tip_percentage)

tax_amount = price_float * tax_float
tip_amount = price_float * tip_float
total = price_float + tax_amount + tip_amount

print(f"Price: ${price_float:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Tip: ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")


print("\n" + "="*50)

# YOUR CODE HERE - Create a unit converter:
# Convert between units like miles/kilometers or Celsius/Fahrenheit
# YOUR CODE HERE:
# 🧭 Simple Unit Converter (no logic, prints all conversions)

print("\n🔁 Unit Converter")

# Ask for a value
value = input("Enter a number to convert: ")
num = float(value)

# Do various conversions
miles_to_km = num * 1.60934
km_to_miles = num / 1.60934
celsius_to_fahrenheit = (num * 9/5) + 32
fahrenheit_to_celsius = (num - 32) * 5/9

# Print all conversions
print(f"{num} miles = {miles_to_km:.2f} kilometers")
print(f"{num} kilometers = {km_to_miles:.2f} miles")
print(f"{num}°C = {celsius_to_fahrenheit:.2f}°F")
print(f"{num}°F = {fahrenheit_to_celsius:.2f}°C")




print("\n" + "="*50)
