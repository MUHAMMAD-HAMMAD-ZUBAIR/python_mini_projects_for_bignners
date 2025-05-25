# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Python Basics – Variable Scope and Functions
# ------------------------------------------------------

# -------------------------------------
# 🔁 Import Required Module
# -------------------------------------
import random  # Used to simulate dice rolls

# -------------------------------------
# 🎯 Constants
# -------------------------------------
NUM_SIDES = 6  # Number of sides on each die

# -------------------------------------
# 🎲 Function to Roll Two Dice
# -------------------------------------
def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    Shows how variable scope works separately from main().
    """
    die1: int = random.randint(1, NUM_SIDES)  # Roll first die
    die2: int = random.randint(1, NUM_SIDES)  # Roll second die
    total: int = die1 + die2                  # Calculate total
    print("🎲 Rolling two dice...")
    print(f"🎯 Die 1: {die1}, 🎯 Die 2: {die2}, 🎯 Total: {total}\n")

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    die1: int = 10  # This die1 is local to main()
    print("🔍 die1 in main() starts as:", die1, "\n")

    # Roll dice three times
    roll_dice()
    roll_dice()
    roll_dice()

    # Check if die1 value changed in main()
    print("🔍 die1 in main() after rolls is still:", die1)

# -------------------------------------
# 🧠 Entry Point
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
