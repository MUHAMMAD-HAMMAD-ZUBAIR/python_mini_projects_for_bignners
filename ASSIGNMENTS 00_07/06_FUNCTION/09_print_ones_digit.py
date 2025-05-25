# ------------------------------------------------------
# 📚 Topic: Finding the Ones Digit of a Number
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program prints the ones digit of a given number.
# ------------------------------------------------------

# -------------------------------------
# 🔢 1. Function to print ones digit
# -------------------------------------
def print_ones_digit(num):
    ones_digit = num % 10  # 🔍 Get remainder when divided by 10
    print(f"🧮 The ones digit is ➡️ {ones_digit}")

# -------------------------------------
# 📥 2. Main function to get input and call helper
# -------------------------------------
def main():
    num = int(input("🔢 Enter a number: "))  # Ask user for number
    print_ones_digit(num)  # Call function to print ones digit

# -------------------------------------
# 🚀 Start the program
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
