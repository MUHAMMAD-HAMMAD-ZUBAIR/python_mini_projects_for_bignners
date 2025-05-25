# ------------------------------------------------------
# 📚 Today class based on: Finding Divisors of a Number
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program prints all divisors of a given number.
# ------------------------------------------------------

# -------------------------------------
# 🧮 1. Function to print divisors
# -------------------------------------
def print_divisors(num: int):
    print(f"🧮 Here are the divisors of {num} ➡️")
    for i in range(num):
        curr_divisor = i + 1  # current divisor candidate
        if num % curr_divisor == 0:  # check if divisor is clean (no remainder)
            print(f"✔️ {curr_divisor}")  # print divisor with emoji

# -------------------------------------
# 🔢 2. Main function to get user input and call print_divisors
# -------------------------------------
def main():
    num = int(input("🔢 Enter a number: "))  # ask user for a number
    print_divisors(num)  # call function to print all divisors

if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# -------------------------------------------------------