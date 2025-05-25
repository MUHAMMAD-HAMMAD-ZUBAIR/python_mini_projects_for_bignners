# ------------------------------------------------------
# 📚 Today class based on: Finding Divisors of a Number
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program finds and prints all divisors of a given number.
# ------------------------------------------------------

# -------------------------------------
# 🔍 1. print_divisors(num) function
# -------------------------------------
def print_divisors(num: int):
    print(f"Here are the divisors of {num} 🧮✨")
    for i in range(1, num + 1):  # Loop from 1 to num inclusive
        if num % i == 0:  # Check if i divides num evenly
            print(f"🔹 {i}")  # Print divisor with emoji bullet

# -------------------------------------
# ▶️ 2. main() function
# -------------------------------------
def main():
    num = int(input("🔢 Enter a number: "))  # Get input from user
    print_divisors(num)  # Call function to print divisors

# ------------------------------------------------------
# ▶️ Program Entry Point
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
