# ------------------------------------------------------
# 📚 Today class based on: Basic Function - Doubling a Number
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program takes a number input from the user,
#     doubles it using a function, and prints the result.
# ------------------------------------------------------

# -------------------------------------
# 🔢 1. double(num) function
# -------------------------------------
def double(num: int) -> int:
    """
    ✖️ Multiplies the input number by 2 and returns the result.
    """
    return num * 2  # ➕ Multiply by 2 and return

# -------------------------------------
# ▶️ 2. main() function - Program starts here
# -------------------------------------
def main():
    num = int(input("🔢 Enter a number: "))  # ⌨️ Take integer input from user
    num_times_2 = double(num)  # 🔢 Call double() function to multiply by 2
    print("✨ Double that is", num_times_2)  # 🖨️ Print the doubled number

# ------------------------------------------------------
# ▶️ Program Entry Point
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
