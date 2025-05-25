# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Python Basics – Guess My Number Game
# ------------------------------------------------------

# -------------------------------------
# 🎮 Guess My Number – Logic & Looping
# -------------------------------------
import random

def main():
    # Generate a secret number randomly between 1 and 99
    secret_number = random.randint(1, 99)

    print("🤔 I am thinking of a number between 1 and 99...")

    # 🎯 Take the first guess
    guess = int(input("👉 Enter a guess: "))

    # 🔁 Repeat until user guesses correctly
    while guess != secret_number:
        if guess < secret_number:
            print("⬆️ Your guess is too low")
        else:
            print("⬇️ Your guess is too high")

        print()  # 👀 Empty line for clean output
        guess = int(input("👉 Enter a new guess: "))

    # ✅ User guessed correctly
    print(f"🎉 Congrats! The number was: {secret_number}")

# 🚀 Main method to start the game
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Guess My Number Program
# ------------------------------------------------------
