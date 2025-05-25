# ------------------------------------------------------
# 🧮 Fibonacci Sequence Generator
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program prints Fibonacci numbers starting from 0 and 1,
#     continuing as long as the values are less than 10,000.
# ------------------------------------------------------

# 🔒 Constant value to stop at
MAX_TERM_VALUE: int = 10000

def main():
    # 🟢 Starting values for Fibonacci sequence
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)

    print("🔢 Fibonacci Sequence up to", MAX_TERM_VALUE, ":\n")

    # 🔁 Loop until current term exceeds the max value
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        # ♻️ Shift terms forward in the sequence
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

# ------------------------------------------------------
# ▶️ Start the Program
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
