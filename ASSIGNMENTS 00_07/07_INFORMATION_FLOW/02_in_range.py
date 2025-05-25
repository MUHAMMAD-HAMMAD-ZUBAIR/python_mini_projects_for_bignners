# ------------------------------------------------------
# 📚 Today class based on: Python Functions - in_range Example
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program defines a function to check if a number lies within a given range (inclusive).
#     It includes examples to demonstrate the function behavior.
# ------------------------------------------------------

# -------------------------------------
# 🔍 Function: in_range
# -------------------------------------
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    # Check if n is greater than or equal to low AND less than or equal to high
    if low <= n <= high:
        return True  # If yes, return True
    return False  # Otherwise, return False

# -------------------------------------
# 🚀 Main function to test in_range()
# -------------------------------------
def main():
    # Print a header for clarity
    print("🔎 Testing in_range function:")

    # Test case 1: 5 between 1 and 10? Expected True
    print("Is 5 in range 1 to 10? ➡️", in_range(5, 1, 10))

    # Test case 2: 0 between 1 and 10? Expected False
    print("Is 0 in range 1 to 10? ➡️", in_range(0, 1, 10))

    # Test case 3: 10 between 10 and 20? Expected True (inclusive check)
    print("Is 10 in range 10 to 20? ➡️", in_range(10, 10, 20))

    # Test case 4: 21 between 10 and 20? Expected False
    print("Is 21 in range 10 to 20? ➡️", in_range(21, 10, 20))

# ------------------------------------------------------
# 🛠️ Required to run main() when this file is executed
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
