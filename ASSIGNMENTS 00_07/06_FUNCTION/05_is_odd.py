# ------------------------------------------------------
# 📚 Today class based on: Even and Odd Numbers
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program prints numbers from 10 to 19 and labels
#     them as "even" or "odd" accordingly.
# ------------------------------------------------------

# -------------------------------------
# 🔢 1. is_odd(value) function
# -------------------------------------
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # 0 if divisible by 2 (even), 1 if odd
    return remainder == 1

# -------------------------------------
# ▶️ 2. main() function
# -------------------------------------
def main():
    for i in range(10, 20):  # Loop from 10 to 19 inclusive
        if is_odd(i):
            print(i, "odd 🔴")
        else:
            print(i, "even 🟢")

# ------------------------------------------------------
# ▶️ Program Entry Point
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
