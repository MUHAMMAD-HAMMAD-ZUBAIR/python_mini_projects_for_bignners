# ------------------------------------------------------
# 💬 Affirmation Reminder
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program keeps asking the user to type a positive affirmation
#     until they type it correctly. Great for motivation and mindset!
# ------------------------------------------------------

# 🌟 The correct affirmation we want the user to type
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # 🧠 Ask user to type the affirmation
    print("📝 Please type the following affirmation exactly:")
    print(f'"{AFFIRMATION}"')

    # ⌨️ Get user input
    user_input = input()

    # 🔁 Keep asking until user types it correctly
    while user_input != AFFIRMATION:
        print("❌ That was not the affirmation.")
        print("🔁 Please type the following affirmation again:")
        print(f'"{AFFIRMATION}"')
        user_input = input()

    # 🎉 Success message
    print("✅ That's right! You're awesome! Keep believing in yourself. 💪")

# ------------------------------------------------------
# ▶️ Start the Program
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
