# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 🏫 Class: Five
# 📅 Date: May 2025
# 📘 Lesson: Generating Random Numbers in Python
# ------------------------------------------------------

import random

N_NUMBERS = 10     # Number of random numbers to print
MIN_VALUE = 1      # Minimum value in range
MAX_VALUE = 100    # Maximum value in range

def main():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)
        print(f"🎲 {num}")

if __name__ == '__main__':
    main()
