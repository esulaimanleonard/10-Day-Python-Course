# ==========================================
# SECTION 1: Basic User Input
# ==========================================

print("SECTION 1: Getting User Input")
print("-" * 27)

# Exercise 1.1: Your First Interactive Program
# Learn how input() waits for user response
name = input("What is your name? ")
print("Hello,", name, "! Nice to meet you!")

age = input("How old are you? ")
print("Wow,", age, "is a great age!")
print("\n" + "="*50)
# YOUR CODE HERE - Create your own input conversation:
# Ask for their favorite color and hobby, then respond

color = input("What is your favorite color? ")
hobby = input("What do you love doing in your free time? ")

print("Nice! " + color + " is such a cool color.")
print("And spending time on", hobby, "sounds fun!")



print("\n" + "="*50)
# Exercise 1.2: Multi-Question Interactive Survey
# Learn to build longer interactive experiences
print("\n🎮 Welcome to the Interest Survey! 🎮")

movie = input("What's your favorite movie? ")
food = input("What's your favorite food? ")
subject = input("What's your favorite school subject? ")

print(f"""
🌟 Your Interest Profile 🌟
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎬 Favorite Movie: {movie}
🍕 Favorite Food: {food}
📚 Favorite Subject: {subject}
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Thanks for sharing!
""")
print("\n" + "="*50)
# YOUR CODE HERE - Create your own survey:
# Ask about travel, weekend activities, or future goals
# Make it engaging with emojis and nice formatting
# YOUR CODE HERE:

print("\n🌍 Let's Talk About You! ✈️")

place = input("🏖️ If you could travel anywhere, where would you go? ")
weekend = input("🎉 What's your favorite thing to do on the weekend? ")
goal = input("🚀 What's one big goal you have for the future? ")

print(f"""
📝 Your Personal Journey 📝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌴 Dream Destination: {place}
🛋️ Weekend Fun: {weekend}
🎯 Future Goal: {goal}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Awesome! Keep dreaming big and doing what you love! 💪
""")




print("\n" + "="*50)
