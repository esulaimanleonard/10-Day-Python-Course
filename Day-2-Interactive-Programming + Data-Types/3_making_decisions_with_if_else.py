# ==========================================
# SECTION 3: Making Decisions with If Statements
# ==========================================

print("SECTION 3: Teaching Programs to Make Decisions")
print("-" * 42)

# Exercise 3.1: Basic If Statements
# Learn how programs can make choices
print("🤖 Decision Making Basics")

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult!")
if age < 18:
    print("You are a minor.")

# Test with numbers
number = int(input("Enter any number: "))
if number > 0:
    print("Your number is positive!")
if number < 0:
    print("Your number is negative!")
if number == 0:
    print("Your number is zero!")

print("\n" + "="*50)

# YOUR CODE HERE - Try basic if statements:
# Ask for a test score and give different messages for different ranges
# YOUR CODE HERE:
# Ask for a test score and give feedback based on the score
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    print("Excellent! You got an A.")
if 80 <= score < 90:
    print("Great job! You got a B.")
if 70 <= score < 80:
    print("Good effort! You got a C.")
if 60 <= score < 70:
    print("You passed with a D.")
if score < 60:
    print("Sorry, you failed the test.")

print("\nThanks for using the program!")


print("\n" + "="*50)

# Exercise 3.2: Complete Decision Systems with Elif
# Learn to handle many possibilities elegantly
print("\n🎯 Grade Calculator")

grade = int(input("Enter your percentage grade: "))

if grade >= 90:
    print("Excellent! You got an A!")
elif grade >= 80:
    print("Great job! You got a B!")
elif grade >= 70:
    print("Good work! You got a C!")
elif grade >= 60:
    print("You passed with a D.")
else:
    print("You need to work harder for a passing grade.")

# Weather advisor
temperature = int(input("What's the temperature outside? "))

if temperature > 80:
    print("It's hot! Wear light clothes and stay hydrated.")
elif temperature > 60:
    print("Nice weather! Perfect for outdoor activities.")
elif temperature > 40:
    print("It's cool. You might want a jacket.")
else:
    print("It's cold! Bundle up with warm clothes.")

print("\n" + "="*50)

# YOUR CODE HERE - Create a multi-choice system:
# Ideas: movie genre recommender, study time advisor
# YOUR CODE HERE:
print("\n🎬 Movie Genre Recommender")

print("How are you feeling today?")
print("1. I want to laugh")
print("2. I feel adventurous")
print("3. I'm in the mood for love")
print("4. I want something scary")
print("5. I just want to relax")

choice = int(input("Enter the number that matches your mood (1–5): "))

if choice == 1:
    print("Try watching a comedy! You'll enjoy some good laughs.")
elif choice == 2:
    print("Check out an action or adventure movie. Something thrilling!")
elif choice == 3:
    print("A romantic movie sounds perfect for you.")
elif choice == 4:
    print("Watch a horror movie if you're up for a scare!")
elif choice == 5:
    print("How about a chill documentary or a calm slice-of-life film?")
else:
    print("That wasn't one of the options. Try again with a number from 1 to 5.")

print("\n" + "="*50)
