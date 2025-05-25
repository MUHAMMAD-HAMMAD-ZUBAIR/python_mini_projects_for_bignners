# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Random Numbers & Dice Simulation
# ------------------------------------------------------

import random  # 📦 Import the random module for dice rolls

# 🎲 Number of sides on each die
NUM_SIDES: int = 6

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # 🎯 Simulate rolling the first and second dice
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # ➕ Calculate the total of both dice
    total: int = die1 + die2

    # 📢 Display the results
    print("🎲 Dice have", NUM_SIDES, "sides each.")
    print("🎯 First die: ", die1)
    print("🎯 Second die:", die2)
    print("🧮 Total of two dice:", total)

# -------------------------------------
# 🧠 Program Entry Point
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
