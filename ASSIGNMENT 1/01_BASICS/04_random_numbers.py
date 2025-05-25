# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Python Basics – Random Number Generation
# ------------------------------------------------------

import random  # 🎲 Importing random module to generate random numbers

# 🎯 Constants
N_NUMBERS: int = 10        # 🔢 Total numbers to generate
MIN_VALUE: int = 1         # 🔽 Minimum value
MAX_VALUE: int = 100       # 🔼 Maximum value

def main():
    """
    🛠️ This function prints 10 random numbers between 1 and 100.
    🎉 Every time you run it, you get a different set of numbers.
    """
    print("🎲 Generating 10 random numbers between 1 and 100:\n")

    for i in range(N_NUMBERS):
        rand_num = random.randint(MIN_VALUE, MAX_VALUE)  # 🎰 Generate random number
        print(f"👉 {rand_num}")  # 📤 Print the number with pointing emoji

# 🚀 Run the main function
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Random Number Generator
# ------------------------------------------------------
