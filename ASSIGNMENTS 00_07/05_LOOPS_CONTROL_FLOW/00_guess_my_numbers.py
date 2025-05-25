# ------------------------------------------------------
# 🎮 Guess My Number Game
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program generates a random number between 1 and 99.
#     The player tries to guess it and receives hints whether the guess is too low or too high.
# ------------------------------------------------------

import random  # Import random to generate random numbers

def main():
    # 🎲 Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)

    print("🤔 I am thinking of a number between 1 and 99...")

    # 🔁 Keep asking until the correct number is guessed
    guess = int(input("🎯 Enter your guess: "))

    while guess != secret_number:
        if guess < secret_number:
            print("⬆️ Your guess is too low.")
        else:
            print("⬇️ Your guess is too high.")
        
        print()  # Print an empty line for spacing
        guess = int(input("🔁 Enter a new guess: "))
    
    # 🎉 Congratulate the user
    print("🎉 Congrats! The number was:", secret_number)

# ------------------------------------------------------
# ▶️ Start the Program
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
