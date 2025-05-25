# ------------------------------------------------------
# 🔢 Double the Number Until It Reaches 100 or More 🚀
# Author: Muhammad Hammad Zubair
# Date: May 2025
# ------------------------------------------------------

def main():
    # Ask user to enter an initial number
    curr_value = int(input("👉 Enter a number: "))

    # Keep doubling while curr_value is less than 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(f"🔄 Doubled value: {curr_value}")

    print("🎉 Done! The value has reached 100 or more!")

# ------------------------------------------------------
# ▶️ Start the Program
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
