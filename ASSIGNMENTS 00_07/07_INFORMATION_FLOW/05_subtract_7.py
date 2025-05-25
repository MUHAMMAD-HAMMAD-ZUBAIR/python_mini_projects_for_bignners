# ------------------------------------------------------
# ➖ Subtract Seven - Interactive Version
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program asks the user for a number, subtracts 7
#     using a helper function, and prints the result.
# ------------------------------------------------------

# -------------------------------------
# 🧮 Function to subtract 7 from input
# -------------------------------------
def subtract_seven(num):
    return num - 7  # Subtract 7 and return result

# -------------------------------------
# 🚀 Main program starts here
# -------------------------------------
def main():
    print("🔢 Welcome to the Subtract Seven Program!")

    try:
        # Ask the user for a number
        user_input = int(input("🔹 Please enter a number: "))

        # Call the helper function
        result = subtract_seven(user_input)

        # Show the result
        print("✅ After subtracting 7, the result is:", result)

    except ValueError:
        # Handle invalid (non-integer) input
        print("❌ Invalid input! Please enter a valid number.")

# ------------------------------------------------------
# 🛠️ Auto-run the main function when script is executed
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# 🎯 End of program
# ------------------------------------------------------
