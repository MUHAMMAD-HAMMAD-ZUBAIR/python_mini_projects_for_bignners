# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Division and Remainder
# ------------------------------------------------------

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # 🧾 Ask the user for the first number (dividend)
    dividend: int = int(input("🔢 Please enter an integer to be divided: "))

    # 🧾 Ask the user for the second number (divisor)
    divisor: int = int(input("➗ Please enter an integer to divide by: "))

    # 🔢 Calculate quotient (integer division)
    quotient: int = dividend // divisor

    # 🔁 Calculate remainder (modulo)
    remainder: int = dividend % divisor

    # 📢 Display the result
    print("✅ The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

# -------------------------------------
# 🧠 Program Entry Point
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
