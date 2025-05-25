# ------------------------------------------------------
# 🤖 Smart Joke Bot - Random & Friendly Version
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     A bot that understands friendly commands and tells random jokes.
#     Fully beginner-friendly, clean, and ready to scale.
# ------------------------------------------------------

import random  # 📦 Importing random module to pick random joke

# -------------------------------------
# 🧾 Constants
# -------------------------------------

# List of supported commands
VALID_COMMANDS = [
    "joke",
    "tell me a joke",
    "say something funny",
    "can you make me laugh?",
    "make me laugh"
]

# List of jokes to choose from
JOKES = [
    "😂 Sophia went to buy milk. Programmer said, 'Get a liter of milk, and if they have eggs, get 12.' She came back with 13 liters. Because they had eggs!",
    "🤣 Why did the Python developer go broke? Because he kept using 'pass' in all his functions!",
    "😆 Why do programmers prefer dark mode? Because the light attracts bugs!",
    "😂 Why don’t robots ever panic? Because they have nerves of steel!",
    "🤣 Debugging: Being the detective in a crime movie where you are also the murderer."
]

# Prompt message
PROMPT = "🎤 What would you like me to do? (Try: 'Tell me a joke'): "
SORRY = "😅 Sorry, I can only tell jokes if you ask nicely. Try something like 'Tell me a joke'."

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # Ask the user for input
    user_input = input(PROMPT).strip().lower()

    # Check if input matches any valid command
    if user_input in VALID_COMMANDS:
        joke = random.choice(JOKES)  # Pick a random joke from the list
        print("\n" + joke)
    else:
        print(SORRY)

# -------------------------------------
# 🛠️ Run the program
# -------------------------------------
if __name__ == '__main__':
    main()
