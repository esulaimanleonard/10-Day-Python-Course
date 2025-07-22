# ==========================================
# SECTION 2: Understanding Data Types
# ==========================================

print("SECTION 2: Data Types in Python")
print("-" * 30)

# Exercise 2.1: Discovering Data Types
# Learn that input() always gives strings and explore other types
user_input = input("Enter any number: ")
print("You entered:", user_input)
print("Type of your input:", type(user_input))

# Compare with actual data types
text_number = "25"
real_number = 25
boolean_value = True
decimal_number = 25.5

print("Text '25':", text_number, "- Type:", type(text_number))
print("Number 25:", real_number, "- Type:", type(real_number))
print("Boolean True:", boolean_value, "- Type:", type(boolean_value))
print("Decimal 25.5:", decimal_number, "- Type:", type(decimal_number))

print("\n" + "="*50)

# YOUR CODE HERE - Create your own data type examples:
# Make variables of each type and print them with their types
# YOUR CODE HERE:

# String example
city = "Lilongwe"
print("City:", city, "- Type:", type(city))

# Integer example
year = 2025
print("Year:", year, "- Type:", type(year))

# Float example
temperature = 36.6
print("Temperature:", temperature, "- Type:", type(temperature))

# Boolean example
is_student = False
print("Is student:", is_student, "- Type:", type(is_student))

# List example
hobbies = ["reading", "coding", "swimming"]
print("Hobbies:", hobbies, "- Type:", type(hobbies))

# Dictionary example
person = {"name": "Leonard", "age": 29}
print("Person Info:", person, "- Type:", type(person))


print("\n" + "="*50)

# Exercise 2.2: Data Type Behaviors
# Learn how different types behave differently
print("\n🔍 How Data Types Behave:")

# Strings can be combined
greeting = "Hello" + " " + "World"
print("String combination:", greeting)

# Numbers can be calculated
number_math = 10 + 15
print("Number calculation:", number_math)

# Interesting behaviors
print("String + String:", "5" + "3")  # This gives "53"
print("Number + Number:", 5 + 3)      # This gives 8
print("String × Number:", "Hi! " * 3)  # This repeats the string

print("\n" + "="*50)

# YOUR CODE HERE - Experiment with data type behaviors:
# Try multiplying strings by numbers, comparing different types
# YOUR CODE HERE:

# Multiplying string by number
repeat_emoji = "😊 " * 4
print("Repeating emoji:", repeat_emoji)

# Adding two floats
sum_floats = 3.5 + 4.2
print("Float + Float:", sum_floats)

# Boolean math
bool_math = True + False  # True is 1, False is 0
print("Boolean math (True + False):", bool_math)

# Comparing a string and an integer (won't work directly)
# Uncommenting this will raise an error:
# print("5" > 3)

# Comparing numbers
print("Is 10 > 5?", 10 > 5)

# Comparing strings
print('"apple" < "banana"?', "apple" < "banana")  # Alphabetical comparison

# Mixing int and float
mixed_math = 7 + 2.5
print("Int + Float:", mixed_math)




print("\n" + "="*50)
