# ==========================================
# SECTION 5: User-Driven Programs
# ==========================================

print("SECTION 5: Programs That Adapt to Users")
print("-" * 37)

# Exercise 5.1: Personalized Responses
# Learn to create programs that respond differently to different users
print("👋 Smart Greeting System")

name = input("What's your name? ")
time_of_day = input("Is it morning, afternoon, or evening? ")

# Handle various ways people might respond
time_response = time_of_day.lower()

if "morning" in time_response:
    greeting = f"Good morning, {name}!"
    print(greeting)
    print("Hope you have a great start to your day!")
elif "afternoon" in time_response:
    greeting = f"Good afternoon, {name}!"
    print(greeting)
    print("Hope your day is going well!")
elif "evening" in time_response or "night" in time_response:
    greeting = f"Good evening, {name}!"
    print(greeting)
    print("Hope you have a restful evening!")
else:
    greeting = f"Hello, {name}!"
    print(greeting)
    print("Have a wonderful day!")


print("\n" + "="*50)

# YOUR CODE HERE - Create a personalized study assistant:
# Ask for name, grade level, and subject difficulty
# Give personalized study advice based on their answers
# YOUR CODE HERE:
print("\n📚 Personalized Study Assistant")

# Ask the user for more info
name = input("What's your name? ")
grade = input("What grade level are you in? (e.g., 6, 10, 12) ")
difficulty = input("Are you finding the subject easy, okay, or hard? ").lower()

# Give personalized advice based on how hard the subject feels
if "easy" in difficulty:
    print(f"Nice work, {name}! Since things feel easy in grade {grade}, try exploring more advanced topics to challenge yourself.")
elif "okay" in difficulty or "medium" in difficulty:
    print(f"You're doing well, {name}. Keep practicing regularly to stay strong in your grade {grade} studies.")
elif "hard" in difficulty or "difficult" in difficulty:
    print(f"Don't worry, {name}. It's normal to struggle sometimes in grade {grade}. Break your study sessions into small chunks and ask for help when needed.")
else:
    print(f"Thanks for the info, {name}. Keep up the good effort in grade {grade}!")

print("\n🎯 Keep going—you’ve got this!")


print("\n" + "="*50)

# Exercise 5.2: Dynamic Content Generation
# Learn to create content based on user preferences
print("\n📝 Dynamic Story Generator")

character_name = input("Enter a character name: ")
character_age = int(input("How old is the character? "))
setting = input("Enter a setting (like 'forest' or 'city'): ")
object_found = input("What magical object does the character find? ")

# Create age-appropriate story elements
if character_age < 12:
    adventure_type = "went on a fun adventure"
    challenge = "solve a friendly puzzle"
elif character_age < 18:
    adventure_type = "embarked on an exciting quest"
    challenge = "overcome a challenging obstacle"
else:
    adventure_type = "began a dangerous mission"
    challenge = "face a formidable enemy"

story = f"""
🌟 The Adventure of {character_name} 🌟

{character_name}, age {character_age}, {adventure_type} in a {setting}.
Suddenly, they discovered a mysterious {object_found}!

"What could this {object_found} be?" wondered {character_name}.

Their mission: {challenge} using the power of the {object_found}.

And so the adventure began...
"""

print(story)

print("\n" + "="*50)

# YOUR CODE HERE - Create a recipe customizer:
# Ask for dietary preferences and generate a custom recipe description
# YOUR CODE HERE:
print("\n🍽️ Custom Recipe Generator")

# Ask for user input
user_name = input("What's your name? ")
diet = input("Do you prefer vegetarian, vegan, or non-vegetarian meals? ").lower()
spice_level = input("Do you like it mild, medium, or spicy? ").lower()
main_ingredient = input("What's your favorite ingredient to cook with? ")

# Build the custom recipe description
if diet == "vegan":
    base = "a plant-based delight"
elif diet == "vegetarian":
    base = "a hearty vegetarian dish"
elif diet == "non-vegetarian":
    base = "a protein-packed meal"
else:
    base = "a creative dish"

if spice_level == "mild":
    spice_description = "with gentle flavors perfect for a calm meal"
elif spice_level == "medium":
    spice_description = "with a balanced touch of spice"
elif spice_level == "spicy":
    spice_description = "with bold, fiery flavors"
else:
    spice_description = "with a surprise twist of taste"

# Final custom recipe description
recipe = f"""
👨‍🍳 Recipe for {user_name}'s Perfect Dish

Today's menu features {base} made with {main_ingredient}, 
{spice_description}. A perfect meal tailored just for you!

Bon appétit, {user_name}!
"""

print(recipe)




print("\n" + "="*50)
