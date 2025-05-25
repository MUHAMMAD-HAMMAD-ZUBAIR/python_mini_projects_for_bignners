# ------------------------------------------------------
# 📚 Today class based on: Chaotic Counting with Probability
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program counts from 1 to 10, but may stop early
#     based on a random chance at each number.
# ------------------------------------------------------

import random  # 🎲 For generating random numbers

# -------------------------------------
# 🎲 DONE_LIKELIHOOD Constant
# -------------------------------------
DONE_LIKELIHOOD = 0.3  # 30% chance to stop counting early

# -------------------------------------
# 🔢 1. chaotic_counting() function
# -------------------------------------
def chaotic_counting():
    """
    Prints numbers from 1 to 10, but stops early based on done() function.
    """
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Stop counting early
        print(curr_num)

# -------------------------------------
# ✅ 2. done() function to decide stopping
# -------------------------------------
def done():
    """
    Returns True randomly with probability DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

# -------------------------------------
# ▶️ 3. main() function - Program starts here
# -------------------------------------
def main():
    print("🚀 I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("🎉 I'm done.")

# ------------------------------------------------------
# ▶️ Program Entry Point
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
