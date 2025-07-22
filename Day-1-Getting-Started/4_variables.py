# ==========================================
# SECTION 4: Variables - Information Storage
# ==========================================

print("SECTION 6: Variables - Your Information Vault")
print("-" * 40)

# Exercise 6.1: Creating and Using Basic Variables
# Learn to store information in labeled containers
name = "Alex"  # String variable
age = 16       # Number variable
is_student = True  # Boolean variable (True/False)

print("Basic Variable Usage:")
print("My name is", name)
print("I am", age, "years old")
print("Am I a student?", is_student)


print("\n" + "="*50)

# YOUR CODE HERE - Create your own basic variables:
# Make variables for: your name, age, favorite color, favorite number
# Then display them in creative sentences
# Creating variables
name = "Leonard"
age = 29
favorite_color = "blue"
favorite_number = 7

# Displaying them in creative sentences
print(f"Hi, my name is {name}.")
print(f"I'm {age} years old and still learning new things every day.")
print(f"My favorite color is {favorite_color} because it's calm and strong.")
print(f"Did you know? My lucky number is {favorite_number} — it just feels right!")

print("\n" + "="*50)


# Exercise 6.2: Modifying and Updating Variables
# Learn that variables can change their values
score = 0
print("Starting score:", score)

score = score + 10  # Add to the score
print("After bonus:", score)

score = score * 2   # Double the score
print("After doubling:", score)


print("\n" + "="*50)

name = "Python Beginner"
print("Status:", name)
name = "Python Expert"  # Variables can be updated
print("New status:", name)


print("\n" + "="*50)

# YOUR CODE HERE - Practice changing variables:
# Create a story where variables change over time
# Ideas: level progression, growing savings, changing weather

# Starting values
player_name = "Leonard the Brave"
level = 1
gold = 100
location = "Forest of Beginnings"

# Game story
print(f"{player_name} begins the adventure at Level {level} in the {location}.")
print(f"With only {gold} gold coins, it's time to explore...\n")

# Level up
level += 1
gold += 50
location = "Cave of Challenges"
print(f"After defeating a wild beast, {player_name} reaches Level {level}!")
print(f"You now have {gold} gold and have entered the {location}.\n")

# Level up again
level += 1
gold += 120
location = "Mountain of Mystery"
print(f"Victory! {player_name} climbs to Level {level}.")
print(f"With {gold} gold, you're now ready to face the secrets of the {location}.")

print("\n" + "="*50)

# Exercise 6.3: Variables in Calculations and Formatting
# Learn to use variables in mathematical operations and formatting
birth_year = 2008
current_year = 2024
calculated_age = current_year - birth_year

print("If you were born in", birth_year)
print("In", current_year, "you would be", calculated_age, "years old")

print("\n" + "="*50)

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equals {fahrenheit}°F")


print("\n" + "="*50)

# YOUR CODE HERE - Create useful calculations with variables:
# Ideas: calculate future age, convert measurements, 
# figure out time differences, calculate totals
# Future age calculator
current_age = 29
years_ahead = 5
future_age = current_age + years_ahead
print(f"In {years_ahead} years, you will be {future_age} years old.")

# Measurement conversion: kilometers to miles
kilometers = 10
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is about {miles:.2f} miles.")

# Time difference: hours between two cities
malawi_time = 14  # 2:00 PM
japan_time = malawi_time + 7  # Japan is +7 hours ahead
print(f"If it's {malawi_time}:00 in Malawi, it's {japan_time}:00 in Japan.")

# Total cost calculator
price_per_item = 3.5
quantity = 4
total_cost = price_per_item * quantity
print(f"Buying {quantity} items at ${price_per_item} each will cost ${total_cost:.2f}.")



print("\n" + "="*50)
