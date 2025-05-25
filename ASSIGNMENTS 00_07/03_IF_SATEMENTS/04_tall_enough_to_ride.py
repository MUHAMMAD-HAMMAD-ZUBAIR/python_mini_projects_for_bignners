# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 🏫 Class: Five
# 📅 Date: May 2025
# 📘 Lesson: Height Checker for Amusement Park Ride with Loop & Emojis
# ------------------------------------------------------

MINIMUM_HEIGHT = 50  # Minimum height to ride (arbitrary units)

def main():
    # Ask user once for height and tell if tall enough
    height = float(input("📏 How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("🎢 You're tall enough to ride! 🎉")
    else:
        print("🚫 You're not tall enough to ride, but maybe next year! 🌱")

def tall_enough_extension():
    # Keep asking until user inputs empty line
    while True:
        user_input = input("📏 How tall are you? (Press Enter to stop) ")
        if user_input == "":
            print("👋 Goodbye! Stay safe!")
            break
        try:
            height = float(user_input)
            if height >= MINIMUM_HEIGHT:
                print("🎢 You're tall enough to ride! 🎉")
            else:
                print("🚫 You're not tall enough to ride, but maybe next year! 🌱")
        except ValueError:
            print("❌ Please enter a valid number!")

# Change this to main() or tall_enough_extension() to test either version
if __name__ == '__main__':
    tall_enough_extension()
