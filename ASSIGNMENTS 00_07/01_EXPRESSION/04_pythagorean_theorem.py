# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Geometry – Right Triangle Hypotenuse
# ------------------------------------------------------

import math  # 🧮 Importing math module to use square root function

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # ✏️ Get lengths of perpendicular sides from the user
    ab: float = float(input("📏 Enter the length of side AB: "))
    ac: float = float(input("📏 Enter the length of side AC: "))

    # 🔢 Apply Pythagorean theorem: hypotenuse² = side1² + side2²
    bc: float = math.sqrt(ab ** 2 + ac ** 2)

    # 📢 Show result to the user
    print("🧮 The length of BC (the hypotenuse) is: " + str(bc))

# -------------------------------------
# 🧠 Program Entry Point
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
